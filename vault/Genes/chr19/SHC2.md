---
symbol: "SHC2"
type: "gene"
col: 5009
ensembl_id: "ENSG00000129946"
name: "SHC adaptor protein 2"
location: "19p13.3"
module: 123
arm: "+"
pooled_cpm: 6.33
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# SHC2

*SHC adaptor protein 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.80× (z +6.4, q 8e-08, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.416× (z -13.5, q 2e-38, down in 29 of 34 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.509× (z -7.3, q 2e-11, down in 21 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZTS3]] (+0.64, fdr 7e-06), [[CACFD1]] (+0.62, fdr 1e-05), [[MAFK]] (+0.60, fdr 9e-06); moves opposite to [[ACTL6A]] (-0.59, fdr 1e-05), [[GSTCD]] (-0.56, fdr 2e-05), [[DUT]] (-0.55, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.80×** | +6.4 | 8e-08 | 22/37 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.82×** | +6.3 | 8e-08 | 17/36 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.66×** | +5.5 | 5e-06 | 19/39 (COLO 205, LoVo, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.69×** | +5.5 | 5e-06 | 18/38 (COLO 205, SHP-77, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +5.3 | 2e-05 | 15/38 (SHP-77, COLO 205, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.59×** | +5.1 | 3e-05 | 15/34 (SW480, PANC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.1 | 3e-05 | 15/36 (LoVo, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.8 | 1e-04 | 1/11 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.36×** | +4.7 | 2e-04 | 11/41 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.56×** | +4.6 | 3e-04 | 12/40 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +4.0 | 0.003 | 10/37 (COLO 205, LoVo, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.007 | 6/34 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +3.4 | 0.028 | 8/38 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.028 | 0/38 | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.028 | 9/33 (COLO 205, LS 180, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.028 | 5/38 (NCI-H460, LS 180, …) | all doses, flat | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +3.3 | 0.028 | 5/39 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.028 | 7/37 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.041 | 9/38 (COLO 205, Panc 03.27, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.082 | 4/38 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.084 | 6/36 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.090 | 10/40 (NCI-H1792, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.416×** | -13.5 | 2e-38 | 29/34 (SW 900, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.326×** | -12.2 | 1e-31 | 27/39 (SW 900, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.370×** | -10.8 | 8e-25 | 25/39 (SW 900, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.413×** | -9.2 | 5e-18 | 28/33 (SW 900, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.458×** | -8.5 | 3e-15 | 25/40 (SW 900, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.489×** | -7.5 | 8e-12 | 24/33 (RKO, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.509×** | -7.3 | 2e-11 | 21/36 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -5.9 | 2e-07 | 15/31 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.358×** | -5.8 | 3e-07 | 20/35 (Panc 03.27, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -4.6 | 2e-04 | 16/41 (BT-474, HepG2/C3A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.453×** | -4.5 | 4e-04 | 16/38 (BT-474, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.669×** | -4.3 | 7e-04 | 16/39 (A-172, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.683×** | -4.1 | 0.002 | 15/39 (AsPC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -4.1 | 0.002 | 13/32 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.530×** | -3.6 | 0.012 | 5/32 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.05 µM |  | **0.726×** | -3.2 | 0.050 | 7/36 (CFPAC-1, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.755×** | -3.0 | 0.074 | 7/37 (AsPC-1, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.586×** | -3.0 | 0.074 | 6/27 (SW480, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -2.9 | 0.099 | 7/40 (SW 1271, BT-474, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -1.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 17.5 | 0 | 5 (4 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0997× (z -10.6) |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 10.1 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.156× (z -10.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.184× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 7.23 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 19.8 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.198× (z -10.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[AsPC-1 (line)]] | alt | 6.11 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0959× (z -8.5) |
| [[C32 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 9.52 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 4.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 3.90 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0567× (z -9.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 4.45 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0700× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.156× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTS3]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CACFD1]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MAFK]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[KCP]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PEA15]] | +0.58 | +0.38 / +0.64 | both halves | 7e-05 | pathway: MAPK family signaling cascades |
| [[JUND]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[EBF4]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[WBP2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KRTAP5-AS1]] | +0.57 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[RNF103]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[FAM50A]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.59 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[GSTCD]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DUT]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SRBD1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ASH2L]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[NCAPD3]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MTERF3]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CNOT9]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[NIF3L1]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[FANCM]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PARK7]] ⚠ | -0.49 | -0.54 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXO5]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MCM6]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SHC2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHA10]] | B | EPHA10 activity raises SHC2's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.93× lower at baseline in the lines without EPHA10 | 0.076 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[MTOR]] | B | MTOR activity lowers SHC2's level | compounds that target MTOR: 4 of 8 raise it (Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.353). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, -0.9); signed map (-5.2, 24.2). **Vector** length 73.1, 13.8% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.6 | -13.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.5 | -9.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.4 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -2.1 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SHC adaptor protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:416,589-461,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLI, SCK, SHCB |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 10 pathways, smallest: Signalling to RAS; Signalling to ERKs; VEGFA-VEGFR2 Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P98077](https://www.uniprot.org/uniprotkb/P98077) (SHC-transforming protein 2):

> Signaling adapter that couples activated growth factor receptors to signaling pathway in neurons. Involved in the signal transduction pathways of neurotrophin-activated Trk receptors in cortical neurons (By similarity).

**Summary**, from NCBI Gene [25759](https://www.ncbi.nlm.nih.gov/gene/25759):

> Predicted to enable receptor tyrosine kinase binding activity. Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to be located in cytosol. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29869) · Entrez [25759](https://www.ncbi.nlm.nih.gov/gene/25759) · UniProt [P98077](https://www.uniprot.org/uniprotkb/P98077) · Ensembl [ENSG00000129946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129946)

## Data

Gene col 5009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5009); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5009]; `tensor/DDL_lfc|DDL_z.npy` [5009]; `embed/gene_vectors.npy` [5009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5009 or target_col == 5009). Every well: [[SHC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
