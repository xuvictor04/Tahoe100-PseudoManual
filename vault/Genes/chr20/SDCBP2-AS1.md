---
symbol: "SDCBP2-AS1"
type: "gene"
col: 13974
ensembl_id: "ENSG00000234684"
name: "SDCBP2 antisense RNA 1"
location: "20p13"
module: 88
arm: "+"
pooled_cpm: 26.45
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# SDCBP2-AS1

*SDCBP2 antisense RNA 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.15× (z +15.5, q 0e+00, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +10.7, q 9e-25, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.636× (z -6.1, q 5e-07, down in 29 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.722× (z -4.4, q 0.003, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (J82 0.0587×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.101×; ⚠ toxic; cell-cycle shift, explains ~13% of this change); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.226×; ⚠ toxic; unreliable plate only); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW48 0.128×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.415×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW48 0.118×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF655]] (+0.77, fdr 7e-06), [[RAB30-DT]] (+0.73, fdr 1e-05), [[PSMD6-AS1]] (+0.72, fdr 7e-06); moves opposite to [[MPG]] (-0.71, fdr 7e-06), [[EFNA4]] (-0.70, fdr 1e-05), [[NFRKB]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +15.5 | 0e+00 | 42/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +14.9 | 0e+00 | 29/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +13.2 | 2e-37 | 37/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.7 | 9e-25 | 36/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.9 | 3e-07 | 31/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 29/48 (HOP62, NCI-H661, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.012 | 19/47 (SNU-423, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.043 | 17/47 (HepG2/C3A, A549, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.043 | 18/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.043 | 12/48 (RPMI-7951, A-427, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.062 | 14/48 (PANC-1, SHP-77, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.18× | +3.2 | 0.062 | 20/47 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.062 | 11/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.071 | 11/47 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (J82 0.0587×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.101×; ⚠ toxic; cell-cycle shift, explains ~13% of this change); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.226×; ⚠ toxic; unreliable plate only); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW48 0.128×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.415×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW48 0.118×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -6.1 | 5e-07 | 29/47 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.722×** | -4.4 | 0.003 | 24/48 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.018 | 21/47 (RKO, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.779×** | -3.4 | 0.093 | 21/48 (KATO III, MIA PaCa-2, …) | top dose only | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.782× | -3.2 | 0.15 | 10/48 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.793× | -3.2 | 0.15 | 13/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.851× | -3.1 | 0.15 | 9/48 (KATO III, A-172, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.732× | -3.0 | 0.17 | 7/48 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bimatoprost (drug)]] 5 µM |  | 0.856× | -3.0 | 0.17 | 12/48 (SHP-77, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.0× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.48× (z +19.3) | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 36.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[J82 (line)]] | alt | 26.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.29× (z +15.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0587× (z -11.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 29.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.2× (z +23.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 25.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.3× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.22× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 16.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.85× (z +10.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.128× (z -9.0) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.0) |
| [[BT-474 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +10.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.86× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.226× (z -9.1) ⚠ toxic; unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~13% of this change |
| [[SNU-423 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | +0.77 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RAB30-DT]] | +0.73 | +0.80 / +0.53 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | +0.72 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[ST7L]] | +0.72 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[ACYP2]] | +0.71 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[LEKR1]] | +0.70 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[FKRP]] | +0.70 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[TAPT1-AS1]] | +0.70 | +0.73 / +0.56 | both halves | 1e-05 | same gene group |
| [[PPP3CB-AS1]] | +0.69 | +0.74 / +0.40 | both halves | 5e-05 | same gene group |
| [[RGS5]] | +0.69 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[TUG1]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.68 | +0.74 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.71 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[EFNA4]] | -0.70 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[NFRKB]] | -0.68 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.68 | -0.74 / -0.49 | both halves | 1e-05 |  |
| [[MPST]] | -0.68 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.67 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.66 | -0.72 / -0.38 | both halves | 6e-05 |  |
| [[HEBP1]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[DOK4]] | -0.65 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.65 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[CNOT8]] | -0.64 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDCBP2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises SDCBP2-AS1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without ITPR2-AS1 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises SDCBP2-AS1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without WARS2-AS1 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.7, 7.3); signed map (18.9, -25.1). **Vector** length 97.1, 22.0% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | SDCBP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p13 — chr20:1,325,400-1,378,735 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44314) · Entrez [100507495](https://www.ncbi.nlm.nih.gov/gene/100507495) · Ensembl [ENSG00000234684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234684)

## Data

Gene col 13974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13974); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13974]; `tensor/DDL_lfc|DDL_z.npy` [13974]; `embed/gene_vectors.npy` [13974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13974 or target_col == 13974). Every well: [[SDCBP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDCBP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
