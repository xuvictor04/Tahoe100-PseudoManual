---
symbol: "EFCAB6"
type: "gene"
col: 11874
ensembl_id: "ENSG00000186976"
name: "EF-hand calcium binding domain 6"
location: "22q13.2-q13.31"
module: 10
arm: "+"
pooled_cpm: 8.31
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 19
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# EFCAB6

*EF-hand calcium binding domain 6* — 22q13.2-q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.66× (z +17.5, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.323× (z -9.1, q 6e-17, down in 32 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.372× (z -8.0, q 5e-13, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHI1-DT]] (+0.79, fdr 7e-06), [[CFAP43]] (+0.75, fdr 7e-06), [[RABL2A]] (+0.75, fdr 7e-06); moves opposite to [[PACC1]] (-0.66, fdr 1e-05), [[ABHD6]] (-0.66, fdr 2e-05), [[MCOLN2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[OSCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.66×** | +17.5 | 0e+00 | 37/37 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +10.5 | 2e-23 | 30/34 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +6.5 | 1e-08 | 21/40 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.4 | 3e-08 | 24/43 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +5.3 | 1e-05 | 28/42 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +5.2 | 2e-05 | 4/13 (SW1417, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +5.0 | 4e-05 | 24/41 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.0 | 4e-05 | 23/36 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +4.5 | 4e-04 | 22/42 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.48×** | +4.5 | 4e-04 | 15/43 (NCI-H1573, A498, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.70×** | +4.3 | 0.001 | 15/42 (A-427, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.001 | 18/40 (KATO III, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.002 | 14/42 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +4.0 | 0.003 | 20/41 (SW480, NCI-H23, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.46×** | +3.6 | 0.012 | 11/43 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.012 | 11/42 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.28×** | +3.5 | 0.018 | 8/41 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.023 | 10/43 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.323×** | -9.1 | 6e-17 | 32/42 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.372×** | -8.0 | 5e-13 | 30/41 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.413×** | -7.1 | 2e-10 | 26/38 (SW480, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.418×** | -7.0 | 3e-10 | 30/41 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.435×** | -6.7 | 2e-09 | 30/42 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.485×** | -5.6 | 2e-06 | 22/33 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.506×** | -5.5 | 3e-06 | 24/42 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.668×** | -4.6 | 3e-04 | 23/43 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.566×** | -4.6 | 3e-04 | 26/42 (AN3 CA, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -4.3 | 8e-04 | 22/40 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.384×** | -4.0 | 0.003 | 18/37 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.630×** | -3.7 | 0.009 | 16/40 (CFPAC-1, KATO III, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -3.6 | 0.016 | 20/39 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.435×** | -3.5 | 0.019 | 10/39 (MIA PaCa-2, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.560×** | -3.3 | 0.033 | 11/43 (SW480, SW 1088, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -3.2 | 0.049 | 10/43 (SW480, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.679×** | -3.1 | 0.059 | 14/42 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -3.0 | 0.074 | 18/41 (RPMI-7951, A549, …) | rises with dose |  |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.675×** | -3.0 | 0.078 | 10/40 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.684×** | -2.9 | 0.089 | 13/40 (AN3 CA, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.6 | 2 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.0787× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -11.8) |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0246× (z -17.5) |
| [[HOP62 (line)]] | alt | 20.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0822× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 9.76 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0479× (z -12.0) ⚠ toxic |
| [[A549 (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.111× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 9.04 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.0845× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 12.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 4.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.40 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +8.5) | [[Drospirenone (drug)]] 0.5 µM 0.0782× (z -8.8) |
| [[PANC-1 (line)]] | alt | 3.13 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.60× (z +11.5) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0731× (z -9.1) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0640× (z -12.1) |
| [[A498 (line)]] | wt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.4) | — |
| [[H4 (line)]] | wt | 8.31 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0306× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 6.07 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0774× (z -9.6) |
| [[LoVo (line)]] | wt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0691× (z -10.7) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 4.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +9.4) | — |
| [[RKO (line)]] | wt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +9.9) | — |
| [[A-427 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | +0.79 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[CFAP43]] | +0.75 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[RABL2A]] | +0.75 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.74 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.73 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[AK8]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.72 | +0.80 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.71 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[DNAI4]] | +0.71 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[ZRANB2-DT]] | +0.71 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.70 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[CAPN3]] | +0.70 | +0.73 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.66 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ABHD6]] | -0.66 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MCOLN2]] | -0.65 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[DNMT3B]] | -0.64 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.62 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ANKS6]] | -0.62 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[BLVRA]] | -0.62 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[GNA12]] | -0.62 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[KLHL8]] | -0.62 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[WASF3]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP8]] | -0.61 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.61 | -0.57 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EFCAB6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CRB1]] | B | CRB1 activity raises EFCAB6's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without CRB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[LPAR3]] | B | LPAR3 activity raises EFCAB6's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without LPAR3 | 0.080 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[ARAP3]] | B | ARAP3 activity raises EFCAB6's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.22× lower at baseline in the lines without ARAP3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[MAP2K1]] | B | MAP2K1 activity lowers EFCAB6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSCP1]] | B | EFCAB6 activity raises OSCP1's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without EFCAB6 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[BLVRA]] | B | EFCAB6 activity raises BLVRA's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without EFCAB6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[METTL6]] | B | EFCAB6 activity raises METTL6's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without EFCAB6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[SUMF1]] | B | EFCAB6 activity raises SUMF1's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without EFCAB6 | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[LMLN]] | B | EFCAB6 activity raises LMLN's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without EFCAB6 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[SH3PXD2B]] | B | EFCAB6 activity raises SH3PXD2B's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without EFCAB6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[ARAP3]] | B | EFCAB6 activity raises ARAP3's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without EFCAB6 | 0.052 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[AMZ2]] | B | EFCAB6 activity raises AMZ2's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without EFCAB6 | 0.054 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[AK8]] | B | EFCAB6 activity raises AK8's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without EFCAB6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[CASC2]] | B | EFCAB6 activity raises CASC2's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without EFCAB6 | 0.065 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[LINC00663]] | B | EFCAB6 activity raises LINC00663's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.91× lower at baseline in the lines without EFCAB6 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[PBLD]] | B | EFCAB6 activity raises PBLD's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without EFCAB6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.3, 20.0); signed map (29.6, -11.9). **Vector** length 69.2, 13.5% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +17.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.4 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2-q13.31 — chr22:43,528,744-43,812,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23588, DJBP, HSCBCIP1, KIAA1672, dJ185D5.1 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5THR3](https://www.uniprot.org/uniprotkb/Q5THR3) (EF-hand calcium-binding domain-containing protein 6):

> Negatively regulates the androgen receptor by recruiting histone deacetylase complex, and protein DJ-1 antagonizes this inhibition by abrogation of this complex. Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating (By similarity).

**Summary**, from NCBI Gene [64800](https://www.ncbi.nlm.nih.gov/gene/64800):

> This gene encodes a protein which directly binds the oncogene DJ-1 and androgen receptor to form a ternary complex in cells. This binding protein recruits histone-deacetylase complexes in order to repress transcription activity of androgen receptor. This protein may also play a role in spermatogenesis and fertilization. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:24204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24204) · Entrez [64800](https://www.ncbi.nlm.nih.gov/gene/64800) · UniProt [Q5THR3](https://www.uniprot.org/uniprotkb/Q5THR3) · Ensembl [ENSG00000186976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186976)

## Data

Gene col 11874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11874); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11874]; `tensor/DDL_lfc|DDL_z.npy` [11874]; `embed/gene_vectors.npy` [11874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11874 or target_col == 11874). Every well: [[EFCAB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
