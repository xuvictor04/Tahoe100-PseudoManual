---
symbol: "MRPL45P2"
type: "gene"
col: 16593
ensembl_id: "ENSG00000291120"
name: ""
location: ""
module: 172
arm: "+"
pooled_cpm: 18.02
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# MRPL45P2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +5.8, q 4e-06, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.590× (z -6.8, q 5e-09, down in 29 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.501× (z -4.7, q 3e-04, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.0747×, MIA PaCa-2 0.137×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.172×, PANC-1 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.233×, SW480 0.313×; ⚠ cell-cycle shift, explains ~40% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (RKO 0.0887×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.108×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.241×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.75, fdr 7e-06), [[N4BP2L2]] (+0.69, fdr 7e-06), [[ATE1OSP]] (+0.68, fdr 1e-05); moves opposite to [[POGLUT2]] (-0.62, fdr 2e-05), [[APMAP]] (-0.62, fdr 3e-05), [[GUSB]] (-0.62, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.8 | 4e-06 | 27/47 (A-427, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.1 | 1e-04 | 28/46 (HT-29, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 19/46 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.002 | 21/45 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.40×** | +4.2 | 0.003 | 18/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.003 | 15/46 (NCI-H1573, HepG2/C3A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.022 | 19/47 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.043 | 14/46 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.043 | 13/46 (HepG2/C3A, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.079 | 18/46 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.26× | +3.1 | 0.11 | 8/47 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16593.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.0747×, MIA PaCa-2 0.137×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.172×, PANC-1 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.233×, SW480 0.313×; ⚠ cell-cycle shift, explains ~40% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (RKO 0.0887×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.108×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.590×** | -6.8 | 5e-09 | 29/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.598×** | -6.4 | 5e-08 | 31/44 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.616×** | -6.3 | 7e-08 | 25/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.661×** | -5.3 | 1e-05 | 25/46 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.501×** | -4.7 | 3e-04 | 24/47 (SNU-1, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.687×** | -4.7 | 3e-04 | 14/28 (LOX-IMVI, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.720×** | -4.2 | 0.002 | 21/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -4.1 | 0.003 | 18/46 (NCI-H1792, A-427, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.739×** | -3.9 | 0.006 | 20/44 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.752×** | -3.7 | 0.014 | 19/40 (HCT15, SK-MEL-2, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.626×** | -3.2 | 0.078 | 7/25 (NCI-H1573, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -13.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 25.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 13.6 | 0 | 2 | — | [[Naproxen (drug)]] 0.05 µM 0.0887× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0747× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[H4 (line)]] | wt | 18.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.108× (z -10.1) |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.135× (z -12.4) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -9.4) |
| [[A-172 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.75 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[HMGA1P4]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MRPL45]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ZNF546]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.66 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.66 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TBCA]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.66 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[MAU2]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.65 | +0.70 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.62 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[APMAP]] | -0.62 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[GUSB]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.61 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GPD1L]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[FAM102B]] | -0.61 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[MPP1]] | -0.60 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TMEM106C]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CLSTN1]] | -0.59 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[PIK3R2]] | -0.59 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[SNX30]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL45P2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, 12.2); signed map (0.2, -5.5). **Vector** length 87.6, 18.1% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | -4.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -4.8 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Salicylic acid (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

> [!warning] No registry record
> MRPL45P2 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16593); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16593]; `tensor/DDL_lfc|DDL_z.npy` [16593]; `embed/gene_vectors.npy` [16593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16593 or target_col == 16593). Every well: [[MRPL45P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL45P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
