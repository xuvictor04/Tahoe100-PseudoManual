---
symbol: "TP53INP2"
type: "gene"
col: 1233
ensembl_id: "ENSG00000078804"
name: "tumor protein p53 inducible nuclear protein 2"
location: "20q11.22"
module: 59
arm: "+"
pooled_cpm: 11.97
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 19
n_dd_up_clean: 24
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TP53INP2

*tumor protein p53 inducible nuclear protein 2* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.76× (z +18.7, q 0e+00, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.566× (z -7.4, q 9e-11, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEU1]] (+0.69, fdr 7e-06), [[RNF103]] (+0.62, fdr 1e-05), [[DUSP8]] (+0.61, fdr 7e-06); moves opposite to [[ORC5]] (-0.62, fdr 1e-05), [[WDR36]] (-0.61, fdr 1e-05), [[IPO11]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BDKRB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.76×** | +18.7 | 0e+00 | 36/42 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.84×** | +8.0 | 4e-13 | 28/46 (HOP62, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.68×** | +6.5 | 1e-08 | 25/45 (HT-29, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.40×** | +6.3 | 5e-08 | 17/47 (BT-474, HT-29, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +6.3 | 5e-08 | 27/46 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.0 | 1e-07 | 21/43 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 21/45 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 21/48 (KATO III, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.7 | 1e-04 | 12/35 (NCI-H2030, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 3e-04 | 20/47 (J82, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.90×** | +4.4 | 6e-04 | 13/46 (BT-474, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +4.3 | 9e-04 | 13/47 (HT-29, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 17/44 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +4.0 | 0.002 | 12/47 (HT-29, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 10/45 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.010 | 11/47 (HT-29, A-427, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.010 | 12/45 (HT-29, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -7.4 | 9e-11 | 27/46 (BT-474, COLO 205, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -5.6 | 8e-06 | 25/39 (NCI-H2030, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -5.3 | 2e-05 | 23/46 (COLO 205, HOP62, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.495×** | -4.8 | 3e-04 | 18/45 (HT-29, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.782×** | -4.5 | 8e-04 | 16/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.789×** | -4.3 | 0.001 | 17/47 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.736×** | -4.0 | 0.006 | 10/46 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Megestrol (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.025 | 10/47 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.768×** | -3.4 | 0.036 | 7/47 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.036 | 9/45 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.772×** | -3.3 | 0.043 | 11/46 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.046 | 9/46 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.768×** | -3.3 | 0.046 | 10/42 (RPMI-7951, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.3 | 0.046 | 11/46 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.046 | 16/46 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.631×** | -3.1 | 0.064 | 8/46 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | **0.634×** | -3.1 | 0.067 | 8/45 (KATO III, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **0.641×** | -3.0 | 0.082 | 8/45 (KATO III, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0223× (z -11.1) |
| [[J82 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +16.0) | — |
| [[KATO III (line)]] | alt | 15.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.54 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +17.1) | — |
| [[A-172 (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.293× (z -8.5) |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0904× (z -9.6) |
| [[HOP62 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +15.6) | — |
| [[Hs 766T (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.4) | — |
| [[LoVo (line)]] | wt | 7.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 30.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -9.3) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +12.4) | — |
| [[SW480 (line)]] | alt | 6.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +12.9) | — |
| [[A-427 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEU1]] | +0.69 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[RNF103]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ATP6V0C]] | +0.61 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[MTHFR]] | +0.59 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[KRTAP5-AS1]] | +0.59 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[DUSP16]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ERF]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[PNPLA2]] | +0.56 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[BMF]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[JUND]] | +0.55 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC5]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[WDR36]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[IPO11]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[CDC123]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.60 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[MRPS35]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[DKC1]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[EARS2]] | -0.58 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PARGP1]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HAUS6]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[TSEN2]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[WDR3]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDKRB2]] | B | BDKRB2 activity strengthens TP53INP2's drug response | lines that do not express BDKRB2 (17) vs lines expressing it (30) | the lines without BDKRB2 respond 0.71× as strongly (z diff +0.78); rises at some drug-doses, falls at others (40% from rises): Ixazomib citrate 0.5 µM: 0.80x vs 0.47x (z diff +2.3); PH-797804 5 µM: 0.48x vs 0.29x (z diff +1.8); Cepharanthine 5 µM: 1.23x vs 1.41x (z diff +1.1) | 0.065 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; target measured in part of the lines; rises at some drug-doses, falls at others |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.3, -47.2); signed map (-8.8, 7.9). **Vector** length 103, 22.7% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +18.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.7 | +6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +8.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p53 inducible nuclear protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,704,339-34,713,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21759, FLJ23500, DKFZp434B2411, DKFZp434O0827, dJ1181N3.1, PINH, DOR; previously C20orf110 |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXH6](https://www.uniprot.org/uniprotkb/Q8IXH6) (Tumor protein p53-inducible nuclear protein 2):

> Dual regulator of transcription and autophagy. Positively regulates autophagy and is required for autophagosome formation and processing. May act as a scaffold protein that recruits MAP1LC3A, GABARAP and GABARAPL2 and brings them to the autophagosome membrane by interacting with VMP1 where, in cooperation with the BECN1-PI3-kinase class III complex, they trigger autophagosome development. Acts as a transcriptional activator of THRA.

**Summary**, from NCBI Gene [58476](https://www.ncbi.nlm.nih.gov/gene/58476):

> The protein encoded by this gene promotes autophagy and is essential for proper autophagosome formation and processing. In addition, the encoded protein can enhance rDNA transcription by helping in the assembly of the POLR1/RNA polymerase I preinitiation complex. Finally, this protein serves as a transcriptional activator for some genes. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:16104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16104) · Entrez [58476](https://www.ncbi.nlm.nih.gov/gene/58476) · UniProt [Q8IXH6](https://www.uniprot.org/uniprotkb/Q8IXH6) · Ensembl [ENSG00000078804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078804)

## Data

Gene col 1233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1233); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1233]; `tensor/DDL_lfc|DDL_z.npy` [1233]; `embed/gene_vectors.npy` [1233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1233 or target_col == 1233). Every well: [[TP53INP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP53INP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
