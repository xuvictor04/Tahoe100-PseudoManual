---
symbol: "EIF2AK3"
type: "gene"
col: 10208
ensembl_id: "ENSG00000172071"
name: "eukaryotic translation initiation factor 2 alpha kinase 3"
location: "2p11.2"
module: 56
arm: "+"
pooled_cpm: 158.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 36
n_dd_up_clean: 4
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# EIF2AK3

*eukaryotic translation initiation factor 2 alpha kinase 3* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.67× (z +6.7, q 1e-08, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.248× (z -17.5, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.619× (z -8.2, q 3e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC11]] (+0.86, fdr 7e-06), [[SRP54]] (+0.84, fdr 7e-06), [[ACBD3]] (+0.82, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.64, fdr 1e-05), [[UTP20]] (-0.62, fdr 1e-05), [[ATE1]] (-0.62, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.67×** | +6.7 | 1e-08 | 39/49 (A-427, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +5.5 | 1e-05 | 35/48 (A-172, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.050 | 25/49 (SHP-77, HT-29, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.068 | 23/49 (SW1417, SHP-77, …) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.25 | 28/48 (A498, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.248×** | -17.5 | 0e+00 | 43/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.301×** | -15.7 | 0e+00 | 45/49 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.498×** | -8.4 | 8e-15 | 37/45 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.619×** | -8.2 | 3e-14 | 44/48 (HS-578T, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.532×** | -7.9 | 3e-13 | 37/48 (A498, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.551×** | -7.5 | 8e-12 | 38/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -6.9 | 5e-10 | 36/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.695×** | -6.1 | 8e-08 | 36/48 (A549, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.6 | 2e-06 | 33/49 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.640×** | -5.6 | 2e-06 | 36/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.650×** | -5.4 | 4e-06 | 31/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -5.2 | 1e-05 | 26/48 (HS-578T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.675×** | -4.9 | 4e-05 | 37/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.686×** | -4.7 | 1e-04 | 35/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.714×** | -4.2 | 0.001 | 36/49 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.001 | 29/48 (H4, A498, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.720×** | -4.1 | 0.001 | 32/48 (NCI-H1792, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.725×** | -4.0 | 0.002 | 36/49 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.727×** | -4.0 | 0.002 | 28/49 (HT-29, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 345 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -14.4) |
| [[HS-578T (line)]] | alt | 212 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 117 | 6 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.32× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 246 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.7) |
| [[Hs 766T (line)]] | wt | 145 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.363× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 259 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 225 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.401× (z -9.6) |
| [[HOP62 (line)]] | alt | 209 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.344× (z -10.9) |
| [[A-427 (line)]] | wt | 98.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.440× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.411× (z -10.2) |
| [[A-172 (line)]] | wt | 175 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.59× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -15.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -18.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -9.2) |
| [[H4 (line)]] | wt | 283 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 158 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 75.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -12.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 130 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC11]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[SRP54]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.82 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.81 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.79 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 567 |
| [[COG6]] | +0.79 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.78 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[COPA]] | +0.78 | +0.80 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.64 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[UTP20]] | -0.62 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ATE1]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises EIF2AK3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.43× lower at baseline in the lines without SNHG18 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[SYVN1]] | C | SYVN1's natural level strengthens EIF2AK3's drug response | SYVN1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.43; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[YIPF2]] | C | YIPF2's natural level strengthens EIF2AK3's drug response | YIPF2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.38; direction not clear | 0.072 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, -34.1); signed map (-50.4, 11.1). **Vector** length 145, 58.5% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.71 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.72 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.72 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.2 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.5 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.0 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 alpha kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:88,556,741-88,691,518 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEK, PERK |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 2 alpha kinases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 13 pathways, smallest: ALK mutants bind TKIs; Modulation of host responses by IFN-stimulated genes; PERK regulates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ5](https://www.uniprot.org/uniprotkb/Q9NZJ5) (Eukaryotic translation initiation factor 2-alpha kinase 3):

> Metabolic-stress sensing protein kinase that phosphorylates the alpha subunit of eukaryotic translation initiation factor 2 (EIF2S1/eIF-2-alpha) in response to various stress, such as unfolded protein response (UPR). Key effector of the integrated stress response (ISR) to unfolded proteins: EIF2AK3/PERK specifically recognizes and binds misfolded proteins, leading to its activation and EIF2S1/eIF-2-alpha phosphorylation. EIF2S1/eIF-2-alpha phosphorylation in response to stress converts …

**Summary**, from NCBI Gene [9451](https://www.ncbi.nlm.nih.gov/gene/9451):

> The protein encoded by this gene phosphorylates the alpha subunit of eukaryotic translation-initiation factor 2, leading to its inactivation, and thus to a rapid reduction of translational initiation and repression of global protein synthesis. This protein is thought to modulate mitochondrial function. It is a type I membrane protein located in the endoplasmic reticulum (ER), where it is induced by ER stress caused by malfolded proteins. Mutations in this gene are associated with …

**Accessions** — [HGNC:3255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3255) · Entrez [9451](https://www.ncbi.nlm.nih.gov/gene/9451) · UniProt [Q9NZJ5](https://www.uniprot.org/uniprotkb/Q9NZJ5) · Ensembl [ENSG00000172071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172071)

## Data

Gene col 10208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10208); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10208]; `tensor/DDL_lfc|DDL_z.npy` [10208]; `embed/gene_vectors.npy` [10208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10208 or target_col == 10208). Every well: [[EIF2AK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2AK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
