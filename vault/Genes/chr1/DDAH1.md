---
symbol: "DDAH1"
type: "gene"
col: 7748
ensembl_id: "ENSG00000153904"
name: "dimethylarginine dimethylaminohydrolase 1"
location: "1p22.3"
module: 120
arm: "+"
pooled_cpm: 133.61
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# DDAH1

*dimethylarginine dimethylaminohydrolase 1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +9.6, q 7e-19, up in 27 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.35× (z +7.4, q 2e-11, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.595× (z -8.6, q 4e-15, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN2]] (+0.77, fdr 7e-06), [[CCN1]] (+0.72, fdr 7e-06, ⚠ same locus), [[CRIM1]] (+0.69, fdr 7e-06), [[CDK6]] (+0.69, fdr 7e-06); moves opposite to [[EMC2]] (-0.59, fdr 1e-05), [[TOM1]] (-0.59, fdr 1e-05), [[BLVRB]] (-0.57, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CCN1]] → it (grade B ⚠); 12 go from it, the strongest it → [[LATS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +9.6 | 7e-19 | 27/45 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.8 | 2e-12 | 23/41 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +7.4 | 2e-11 | 28/46 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.8 | 1e-09 | 24/46 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 2e-08 | 22/45 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.6 | 2e-06 | 23/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.6 | 4e-04 | 23/45 (CFPAC-1, LS 180, …) | rises with dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.005 | 22/45 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +3.8 | 0.011 | 24/45 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.024 | 19/44 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.5 | 0.027 | 16/45 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +3.4 | 0.028 | 21/44 (A-172, SW 900, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.035 | 13/46 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -8.6 | 4e-15 | 39/45 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -8.1 | 2e-13 | 36/45 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.608×** | -7.8 | 1e-12 | 39/45 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.593×** | -4.5 | 7e-04 | 24/43 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.753×** | -4.5 | 7e-04 | 25/44 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 0.001 | 26/44 (NCI-H2030, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 0.848× | -3.9 | 0.009 | 17/45 (J82, HS-578T, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.806×** | -3.6 | 0.024 | 23/45 (RKO, LS 180, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.809×** | -3.5 | 0.028 | 22/45 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.029 | 19/45 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.809×** | -3.4 | 0.037 | 24/44 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -3.3 | 0.042 | 16/45 (LOX-IMVI, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.872× | -3.2 | 0.059 | 12/45 (SNU-1, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.826×** | -3.2 | 0.063 | 21/45 (LOX-IMVI, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 346 | 0 | 12 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.201× (z -14.5) |
| [[RKO (line)]] | wt | 417 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 206 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 82.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.423× (z -10.0) |
| [[HT-29 (line)]] | alt | 147 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +10.6) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.448× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.15× (z +14.4) | [[Adagrasib (drug)]] 0.05 µM 0.494× (z -19.5) ⚠ position not correctable |
| [[C-33 A (line)]] | alt | 199 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.253× (z -13.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 70.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 250 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.6) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.403× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -14.4) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.311× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 78.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +23.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.21× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 67.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +9.0) ⚠ toxic; transcription drop | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.299× (z -9.5) |
| [[KATO III (line)]] | alt | 95.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 60.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 88.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[A-427 (line)]] | wt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +10.0) | — |
| [[A498 (line)]] | wt | 58.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -9.3) |
| [[A549 (line)]] | wt | 65.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 91.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[C32 (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.556× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 66.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 257 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +8.9) | — |
| [[LoVo (line)]] | wt | 105 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.519× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 192 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.494× (z -8.6) |
| [[SW1417 (line)]] | alt | 98.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 46.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.75× (z +8.7) | — |
| [[A-172 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN2]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CCN1]] | +0.72 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN; ⚠ same locus (2.4 kb: neighbours can correlate without regulation) |
| [[CRIM1]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CDK6]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SRGAP1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[DLC1]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ENC1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NF2]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SFTA1P]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[PARVA]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CTNNAL1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TOM1]] | -0.59 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RBCK1]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[FTL]] | -0.54 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[TULP3]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MKNK2]] | -0.53 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KCTD7]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.52 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MED10]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN1]] | B | CCN1 activity raises DDAH1's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without CCN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[BNC2]] | B | BNC2 activity raises DDAH1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 1.22× lower at baseline in the lines without BNC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[CLCN4]] | B | CLCN4 activity strengthens DDAH1's drug response | lines that do not express CLCN4 (7) vs lines expressing it (39) | the lines without CLCN4 respond 0.46× as strongly (z diff +1.56); strongest at Homoharringtonine 5 µM: 1.02x vs 1.57x (z diff +5.6) | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SFTA1P]] | B | SFTA1P activity raises DDAH1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without SFTA1P | 0.036 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[TMEM156]] | B | TMEM156 activity raises DDAH1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.33× lower at baseline in the lines without TMEM156 | 0.045 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[CCDC9B]] | B | CCDC9B activity lowers DDAH1's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.90× higher at baseline in the lines without CCDC9B | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[LINC00472]] | B | LINC00472 activity raises DDAH1's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without LINC00472 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[CLCN4]] | B | CLCN4 activity lowers DDAH1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 2.06× higher at baseline in the lines without CLCN4 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADGRG6]] | B | ADGRG6 activity raises DDAH1's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without ADGRG6 | 0.068 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LATS2]] | C | DDAH1 activity raises LATS2's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.56× lower at baseline in the lines without DDAH1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[NG25 (drug)]] 5 µM | C | DDAH1 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.45× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[AT7519 (drug)]] 5 µM | C | DDAH1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.44× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[AMOTL2]] | C | DDAH1 activity raises AMOTL2's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.48× lower at baseline in the lines without DDAH1 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[CDHR3]] | C | DDAH1 activity raises CDHR3's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without DDAH1 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[TEAD1]] | C | DDAH1 activity strengthens TEAD1's drug response | lines that do not express DDAH1 (3) vs lines expressing it (46) | the lines without DDAH1 respond 0.14× as strongly (z diff +3.31); strongest at Homoharringtonine 5 µM: 0.89x vs 2.35x (z diff +8.8) | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[CRIM1]] | C | DDAH1 activity raises CRIM1's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without DDAH1 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[PTPN14]] | C | DDAH1 activity raises PTPN14's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without DDAH1 | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | DDAH1 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 1.43× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | DDAH1 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 1.56× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 5 µM | C | DDAH1 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.57× the cells of the other lines | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | DDAH1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.62× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.5, 12.6); signed map (14.1, 41.1). **Vector** length 148, 47.4% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.6 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.2 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.7 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.6 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.5 | -8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -5.9 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.9 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dimethylarginine dimethylaminohydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,318,481-85,578,363 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDAH |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 2 pathways, smallest: eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94760](https://www.uniprot.org/uniprotkb/O94760) (N(G),N(G)-dimethylarginine dimethylaminohydrolase 1):

> Hydrolyzes N(G),N(G)-dimethyl-L-arginine (ADMA) and N(G)-monomethyl-L-arginine (MMA) which act as inhibitors of NOS. Has therefore a role in the regulation of nitric oxide generation.

**Summary**, from NCBI Gene [23576](https://www.ncbi.nlm.nih.gov/gene/23576):

> This gene belongs to the dimethylarginine dimethylaminohydrolase (DDAH) gene family. The encoded enzyme plays a role in nitric oxide generation by regulating cellular concentrations of methylarginines, which in turn inhibit nitric oxide synthase activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2715) · Entrez [23576](https://www.ncbi.nlm.nih.gov/gene/23576) · UniProt [O94760](https://www.uniprot.org/uniprotkb/O94760) · Ensembl [ENSG00000153904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153904)

## Data

Gene col 7748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7748); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7748]; `tensor/DDL_lfc|DDL_z.npy` [7748]; `embed/gene_vectors.npy` [7748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7748 or target_col == 7748). Every well: [[DDAH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDAH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
