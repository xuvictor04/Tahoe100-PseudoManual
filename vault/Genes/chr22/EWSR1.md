---
symbol: "EWSR1"
type: "gene"
col: 11346
ensembl_id: "ENSG00000182944"
name: "EWS RNA binding protein 1"
location: "22q12.2"
module: 3
arm: "-"
pooled_cpm: 158.33
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# EWSR1

*EWS RNA binding protein 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.62× (z +15.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.632× (z -7.0, q 1e-09, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUBP1]] (+0.83, fdr 7e-06), [[HNRNPM]] (+0.79, fdr 7e-06), [[SRSF1]] (+0.75, fdr 1e-05); moves opposite to [[CIAO2B]] (-0.77, fdr 1e-05), [[NUDT22]] (-0.74, fdr 5e-05), [[COMMD6]] (-0.73, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.62×** | +15.0 | 0e+00 | 48/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +13.6 | 1e-39 | 44/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.39×** | +13.4 | 1e-38 | 47/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.27×** | +12.4 | 2e-33 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.9 | 1e-25 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.9 | 4e-21 | 48/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +9.9 | 4e-21 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +8.5 | 1e-15 | 47/48 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +7.8 | 5e-13 | 44/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +7.7 | 6e-13 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +7.3 | 2e-11 | 37/45 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +6.9 | 2e-10 | 43/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.7 | 8e-10 | 37/49 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 2e-08 | 43/48 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.2 | 2e-08 | 35/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.49×** | +5.7 | 4e-07 | 34/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +5.2 | 8e-06 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 3e-04 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.4 | 3e-04 | 36/48 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -7.0 | 1e-09 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -5.9 | 1e-06 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.8 | 1e-06 | 29/49 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.694×** | -5.6 | 4e-06 | 35/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -4.3 | 0.002 | 34/48 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -3.8 | 0.014 | 30/48 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Thymol (drug)]] 5 µM |  | 0.856× | -3.4 | 0.062 | 18/48 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.804×** | -3.2 | 0.095 | 23/48 (SW480, PANC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.816× | -3.1 | 0.11 | 22/48 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.14 | 22/48 (A498, AsPC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 128 | 11 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +15.8) | [[Belinostat (drug)]] 5 µM 0.483× (z -9.8) |
| [[LoVo (line)]] | wt | 190 | 10 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 10.8× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 128 | 10 (1 ⚠) | 1 | [[Digitoxin (drug)]] 0.05 µM 2.82× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 150 | 8 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.3) |
| [[HOP62 (line)]] | alt | 104 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.5) | — |
| [[A549 (line)]] | wt | 118 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.2) | — |
| [[SW480 (line)]] | alt | 186 | 7 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.54× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 166 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 106 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.3) | — |
| [[A-172 (line)]] | wt | 82.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 162 | 6 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.58× (z +14.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 15.9× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 144 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 218 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 8.20× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 137 | 6 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.23× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 143 | 5 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.97× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 182 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 7.29× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 211 | 5 | 0 | [[PH-797804 (drug)]] 5 µM 7.38× (z +10.8) | — |
| [[KATO III (line)]] | alt | 184 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 197 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 163 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 122 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 255 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.64× (z +10.5) | — |
| [[SW48 (line)]] | wt | 254 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.07× (z +14.2) | — |
| [[A-427 (line)]] | wt | 122 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.29× (z +12.4) | — |
| [[C32 (line)]] | wt | 152 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 129 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.16× (z +10.0) | — |
| [[H4 (line)]] | wt | 108 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 7.57× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 132 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +12.0) | — |
| [[RKO (line)]] | wt | 234 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.26× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 158 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.93× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 194 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.24× (z +10.5) | — |
| [[A498 (line)]] | wt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 212 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.31× (z +9.4) | — |
| [[J82 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.37× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.85× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 147 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.54× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 154 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 187 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.66× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 86.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.48× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 219 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.32× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 246 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 | STRING 492 |
| [[HNRNPM]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; STRING 901 |
| [[SRSF1]] | +0.75 | +0.53 / +0.76 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 799 |
| [[SFPQ]] | +0.73 | +0.53 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 883 |
| [[U2AF2]] | +0.72 | +0.54 / +0.73 | both halves | 1e-05 | same gene group; STRING 623 |
| [[DHX9]] | +0.71 | +0.75 / +0.78 | both halves | 7e-06 | STRING 997 |
| [[ILF3]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 704 |
| [[PIGO]] | +0.70 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[YWHAE]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[HNRNPD]] | +0.70 | +0.53 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 677 |
| [[FECH]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[BCLAF1]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 | STRING 459 |

## Genes that move opposite

*49 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.77 | -0.50 / -0.79 | both halves | 1e-05 |  |
| [[NUDT22]] | -0.74 | -0.40 / -0.80 | both halves | 5e-05 |  |
| [[COMMD6]] | -0.73 | -0.51 / -0.77 | both halves | 1e-05 |  |
| [[MPG]] | -0.72 | -0.39 / -0.80 | both halves | 5e-05 |  |
| [[TRPT1]] | -0.72 | -0.47 / -0.74 | both halves | 2e-05 |  |
| [[DDT]] | -0.72 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[ARID3A]] | -0.70 | -0.58 / -0.74 | both halves | 7e-06 |  |
| [[ING2]] | -0.69 | -0.47 / -0.77 | both halves | 2e-05 |  |
| [[TMEM191A-1]] | -0.69 | -0.36 / -0.74 | both halves | 1e-04 |  |
| [[CIB1]] | -0.69 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[ATP5MK]] | -0.68 | -0.42 / -0.73 | both halves | 4e-05 |  |
| [[VKORC1]] | -0.68 | -0.50 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EWSR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.4, -24.6); signed map (14.6, -38.2). **Vector** length 105, 43.2% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.61 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.63 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.63 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +13.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +13.1 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +13.0 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +10.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | -0.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | +2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | EWS RNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,268,009-29,300,525 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EWS |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; RNA binding motif containing; FET protein family |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01844](https://www.uniprot.org/uniprotkb/Q01844) (RNA-binding protein EWS):

> Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'. Might normally function as a transcriptional repressor. EWS-fusion-proteins (EFPS) may play a role in the tumorigenic process. They may disturb gene expression by mimicking, or interfering with the normal function of CTD-POLII within the transcription initiation complex. They may also contribute to an aberrant activation of the fusion protein target genes.

**Summary**, from NCBI Gene [2130](https://www.ncbi.nlm.nih.gov/gene/2130):

> This gene encodes a multifunctional protein that is involved in various cellular processes, including gene expression, cell signaling, and RNA processing and transport. The protein includes an N-terminal transcriptional activation domain and a C-terminal RNA-binding domain. Chromosomal translocations between this gene and various genes encoding transcription factors result in the production of chimeric proteins that are involved in tumorigenesis. These chimeric proteins usually consist of the …

**Accessions** — [HGNC:3508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3508) · Entrez [2130](https://www.ncbi.nlm.nih.gov/gene/2130) · UniProt [Q01844](https://www.uniprot.org/uniprotkb/Q01844) · Ensembl [ENSG00000182944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182944)

## Data

Gene col 11346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11346); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11346]; `tensor/DDL_lfc|DDL_z.npy` [11346]; `embed/gene_vectors.npy` [11346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11346 or target_col == 11346). Every well: [[EWSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EWSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
