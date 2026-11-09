---
symbol: "SLC17A5"
type: "gene"
col: 4131
ensembl_id: "ENSG00000119899"
name: "solute carrier family 17 member 5"
location: "6q13"
module: 56
arm: "+"
pooled_cpm: 66.05
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 36
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SLC17A5

*solute carrier family 17 member 5* — 6q13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -27.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1A1]] (+0.77, fdr 7e-06), [[EIF2AK3]] (+0.76, fdr 7e-06), [[PDXDC2P-NPIPB14P]] (+0.74, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.70, fdr 7e-06), [[HNRNPK]] (-0.70, fdr 7e-06), [[KRT8P12]] (-0.69, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.064 | 18/48 (Hs 766T, SNU-1, …) | top dose only |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.22× | +3.4 | 0.21 | 11/48 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.24 | 7/49 (KATO III, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -27.6 | 0e+00 | 44/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.271×** | -22.2 | 0e+00 | 43/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.424×** | -20.5 | 0e+00 | 41/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.389×** | -16.1 | 0e+00 | 44/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.408×** | -14.7 | 0e+00 | 42/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.460×** | -12.7 | 7e-35 | 35/43 (SNU-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.478×** | -12.6 | 3e-34 | 44/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.636×** | -10.8 | 3e-25 | 37/48 (HOP62, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.507×** | -10.7 | 7e-25 | 36/45 (NCI-H23, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.525×** | -10.5 | 3e-24 | 37/48 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.662×** | -9.8 | 4e-21 | 42/48 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -9.5 | 1e-19 | 42/49 (HS-578T, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.574×** | -9.4 | 2e-19 | 34/48 (Hs 766T, HS-578T, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.583×** | -9.2 | 2e-18 | 40/49 (RKO, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.580×** | -8.9 | 2e-17 | 37/50 (HS-578T, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.400×** | -8.1 | 1e-14 | 40/48 (LS 180, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.661×** | -6.6 | 9e-10 | 37/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -6.1 | 2e-08 | 29/48 (HOP62, LoVo, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.688×** | -6.1 | 3e-08 | 34/48 (HS-578T, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.681×** | -6.0 | 4e-08 | 34/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.758×** | -4.7 | 6e-05 | 31/48 (A-427, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 90.9 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0472× (z -43.7) |
| [[A498 (line)]] | wt | 82.0 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -36.6) |
| [[Hs 766T (line)]] | wt | 155 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -17.1) |
| [[HOP62 (line)]] | alt | 78.2 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.6) |
| [[A-172 (line)]] | wt | 84.3 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -27.5) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -21.3) |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -26.9) |
| [[RPMI-7951 (line)]] | alt | 87.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -22.7) |
| [[J82 (line)]] | alt | 55.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -19.7) |
| [[NCI-H2347 (line)]] | alt | 89.1 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -24.5) |
| [[A549 (line)]] | wt | 48.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.0) |
| [[H4 (line)]] | wt | 53.2 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 75.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -28.3) |
| [[SW 900 (line)]] | alt | 67.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.7) |
| [[AsPC-1 (line)]] | alt | 69.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -28.7) |
| [[C32 (line)]] | wt | 53.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -23.8) |
| [[HT-29 (line)]] | alt | 58.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 84.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 62.1 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -14.0) |
| [[KATO III (line)]] | alt | 76.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -17.9) |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 72.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -14.5) |
| [[SW480 (line)]] | alt | 50.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 29.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.9) |
| [[LoVo (line)]] | wt | 81.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -15.9) |
| [[PANC-1 (line)]] | alt | 56.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.6) |
| [[RKO (line)]] | wt | 57.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.7) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -13.2) |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.8) |
| [[HCT15 (line)]] | alt | 64.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.5) |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -10.5) |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 60.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 70.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.569× (z -9.2) |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0717× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.6) |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0494× (z -9.9) |
| [[A-427 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1A1]] | +0.77 | +0.77 / +0.69 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[EIF2AK3]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[TULP3]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[COG6]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC22A]] | +0.73 | +0.59 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SDHAP2]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[TTC3]] | +0.72 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[WIPI1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SLC31A1]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[ACBD3]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.70 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.70 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[KRT8P12]] | -0.69 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[TASOR]] | -0.69 | -0.73 / -0.58 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.68 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.65 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[UTP20]] | -0.64 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.64 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[ZNF300]] | -0.63 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[YWHAE]] | -0.63 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[KRR1]] | -0.63 | -0.66 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC17A5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -34.7); signed map (-47.7, 12.4). **Vector** length 128, 44.5% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.59 to 16); *protein secretion* (hallmark, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.4 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.2 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +0.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.2 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.4 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.6 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -10.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.3 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.1 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 17 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,593,379-73,653,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AST, SD, ISSD, NSD, SIALIN, SLD; previously SIASD |
| Gene groups (HGNC) | Solute carrier family 17 |
| Reactome | 14 pathways, smallest: Organic anion transport by SLC5/17/25 transporters; Hyaluronan degradation; Hyaluronan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRA2](https://www.uniprot.org/uniprotkb/Q9NRA2) (Sialin):

> Multifunctional anion transporter that operates via two distinct transport mechanisms, namely proton-coupled anion cotransport and membrane potential-dependent anion transport. Electroneutral proton-coupled acidic monosaccharide symporter, with a sugar to proton stoichiometry of 1:1. Exports glucuronic acid and free sialic acid derived from sialoglycoconjugate degradation out of lysosomes, driven by outwardly directed lysosomal pH gradient. May regulate lysosome function and metabolism of …

**Summary**, from NCBI Gene [26503](https://www.ncbi.nlm.nih.gov/gene/26503):

> This gene encodes a membrane transporter that exports free sialic acids that have been cleaved off of cell surface lipids and proteins from lysosomes. Mutations in this gene cause sialic acid storage diseases, including infantile sialic acid storage disorder and and Salla disease, an adult form. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10933) · Entrez [26503](https://www.ncbi.nlm.nih.gov/gene/26503) · UniProt [Q9NRA2](https://www.uniprot.org/uniprotkb/Q9NRA2) · Ensembl [ENSG00000119899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119899)

## Data

Gene col 4131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4131); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4131]; `tensor/DDL_lfc|DDL_z.npy` [4131]; `embed/gene_vectors.npy` [4131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4131 or target_col == 4131). Every well: [[SLC17A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC17A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
