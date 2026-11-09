---
symbol: "PLAGL2"
type: "gene"
col: 4707
ensembl_id: "ENSG00000126003"
name: "PLAG1 like zinc finger 2"
location: "20q11.21"
module: 16
arm: "+"
pooled_cpm: 15.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PLAGL2

*PLAG1 like zinc finger 2* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.79× (z +6.8, q 3e-09, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.554× (z -7.0, q 1e-09, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -4.7, q 5e-04, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM12]] (+0.68, fdr 7e-06), [[PRRC2A]] (+0.66, fdr 1e-05), [[ZNF256]] (+0.65, fdr 1e-05); moves opposite to [[BIRC6-AS2-1]] (-0.56, fdr 3e-05), [[EOGT-DT]] (-0.56, fdr 7e-06), [[CTBP1-AS]] (-0.55, fdr 8e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[MACO1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF649]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +6.8 | 3e-09 | 35/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +6.8 | 3e-09 | 38/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +5.6 | 5e-06 | 26/48 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +5.5 | 5e-06 | 26/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.002 | 22/47 (LOX-IMVI, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.13 | 18/47 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.20 | 1/48 (LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.554×** | -7.0 | 1e-09 | 24/36 (HEC-1-A, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -5.2 | 5e-05 | 19/27 (HOP62, KATO III, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.7 | 5e-04 | 26/47 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -3.8 | 0.025 | 20/45 (NCI-H23, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.027 | 20/48 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.070 | 15/48 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.830× | -3.2 | 0.13 | 11/48 (NCI-H460, BT-474, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.771× | -3.1 | 0.14 | 17/47 (SNU-423, HepG2/C3A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -10.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 11.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -11.6) |
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0736× (z -13.8) |
| [[C32 (line)]] | wt | 7.32 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0945× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0649× (z -16.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 9.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 7.97 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0819× (z -9.4) |
| [[J82 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[SW480 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM12]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZNF256]] | +0.65 | +0.55 / +0.67 | both halves | 1e-05 | same gene group |
| [[SF3B4]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SRRD]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[USP19]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB9]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF574]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 | same gene group |
| [[MANBAL]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC6-AS2-1]] | -0.56 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[EOGT-DT]] | -0.56 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[CTBP1-AS]] ⚠ | -0.55 | -0.37 / -0.65 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MACO1]] | -0.55 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ATP5PD]] | -0.54 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[KIZ-AS1]] ⚠ | -0.53 | -0.43 / -0.55 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EFCAB14-AS1]] | -0.53 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[ZBTB47-AS1]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MORC3]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RAB6A]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RHOQ-AS1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CNGB3]] | -0.51 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[RPS12]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[FBXL20]] | -0.51 | -0.37 / -0.57 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF649]] | B | ZNF649 activity raises PLAGL2's level | lines that do not express ZNF649 (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without ZNF649 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF577, ZNF681, RPSAP58 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.8, -2.2); signed map (-1.2, -33.0). **Vector** length 66.8, 11.0% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.3 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PLAG1 like zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,192,504-32,207,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF900 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPG8](https://www.uniprot.org/uniprotkb/Q9UPG8) (Zinc finger protein PLAGL2):

> Shows weak transcriptional activatory activity.

**Summary**, from NCBI Gene [5326](https://www.ncbi.nlm.nih.gov/gene/5326):

> Pleiomorphic adenoma gene-like 2 is a zinc-finger protein that recognizes DNA and/or RNA. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9047) · Entrez [5326](https://www.ncbi.nlm.nih.gov/gene/5326) · UniProt [Q9UPG8](https://www.uniprot.org/uniprotkb/Q9UPG8) · Ensembl [ENSG00000126003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126003)

## Data

Gene col 4707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4707); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4707]; `tensor/DDL_lfc|DDL_z.npy` [4707]; `embed/gene_vectors.npy` [4707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4707 or target_col == 4707). Every well: [[PLAGL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAGL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
