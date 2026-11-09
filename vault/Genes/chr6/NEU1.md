---
symbol: "NEU1"
type: "gene"
col: 12863
ensembl_id: "ENSG00000204386"
name: "neuraminidase 1"
location: "6p21.33"
module: 59
arm: "+"
pooled_cpm: 23.52
n_lines_expressing: 48
n_dd_up: 60
n_dd_down: 1
n_dd_up_clean: 50
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# NEU1

*neuraminidase 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 60 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.42× (z +22.8, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.664× (z -4.5, q 0.004, down in 26 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0526×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABARAP]] (+0.73, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[NPC2]] (+0.72, fdr 7e-06), [[FLCN]] (+0.72, fdr 7e-06), [[TP53INP2]] (+0.69, fdr 7e-06); moves opposite to [[CCT6A]] (-0.64, fdr 1e-05), [[CCT5]] (-0.62, fdr 1e-05), [[NUP205]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 60 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.42×** | +22.8 | 0e+00 | 46/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.74×** | +21.7 | 0e+00 | 46/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +21.1 | 0e+00 | 44/46 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.77×** | +17.8 | 0e+00 | 45/45 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.71×** | +10.9 | 1e-25 | 39/46 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.7 | 2e-20 | 39/44 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.33×** | +9.6 | 6e-20 | 40/46 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +9.0 | 1e-17 | 29/45 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.3 | 5e-15 | 40/45 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.1 | 5e-11 | 23/38 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +6.6 | 2e-09 | 35/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +6.3 | 1e-08 | 35/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.3 | 1e-08 | 34/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.2 | 3e-08 | 19/32 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +6.1 | 4e-08 | 31/43 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +6.0 | 6e-08 | 33/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.69×** | +5.9 | 9e-08 | 34/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.64×** | +5.6 | 7e-07 | 31/45 (SNU-423, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.53×** | +5.5 | 1e-06 | 33/46 (KATO III, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12863.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.664×** | -4.5 | 0.004 | 26/45 (HepG2/C3A, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.731× | -3.6 | 0.10 | 21/45 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.741× | -3.2 | 0.30 | 14/45 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 51.3 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 13.3 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +16.9) | — |
| [[PANC-1 (line)]] | alt | 7.70 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +14.4) | — |
| [[RKO (line)]] | wt | 26.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.54× (z +12.7) | — |
| [[A-172 (line)]] | wt | 15.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +15.3) | — |
| [[A549 (line)]] | wt | 9.38 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 16.8× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.3× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 14.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 55.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +16.2) | — |
| [[KATO III (line)]] | alt | 61.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.16× (z +17.0) | — |
| [[SW1417 (line)]] | alt | 41.2 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.57× (z +14.4) | — |
| [[SW480 (line)]] | alt | 15.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +18.1) | — |
| [[A-427 (line)]] | wt | 12.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +12.5) | — |
| [[A498 (line)]] | wt | 18.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 43.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 20.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 25.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.50× (z +12.6) | — |
| [[LoVo (line)]] | wt | 35.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 33.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 44.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.55× (z +15.5) | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.30× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.8× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 67.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.99× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 35.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 62.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.04 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.92× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +15.6) | — |
| [[BT-474 (line)]] | alt | 27.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 8.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +14.9) | — |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0526× (z -13.6) |
| [[C-33 A (line)]] | alt | 7.29 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 19.6× (z +9.2) | — |
| [[C32 (line)]] | wt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +14.9) | — |
| [[SHP-77 (line)]] | alt | 12.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.57× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | +0.73 | +0.79 / +0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NPC2]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[FLCN]] | +0.72 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[TP53INP2]] | +0.69 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[CTSA]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[SAT2]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ZFYVE1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ATP6V0C]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[GRINA]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.62 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GLMP]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6A]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[CCT5]] | -0.62 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[NUP205]] | -0.61 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.58 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[PA2G4]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[BEND3]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[NUDT5]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.56 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[CSE1L]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GMPS]] | -0.56 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[CDC123]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEU1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 11.2% of all compounds | 0.028 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.4, -46.7); signed map (-9.6, 7.2). **Vector** length 106, 32.0% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Amino acids regulate mTORC1* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.1 | +9.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -0.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -1.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.7 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +2.0 |

## What is on record

|  |  |
|---|---|
| Name | neuraminidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,857,659-31,862,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NEU |
| Gene groups (HGNC) | Neuraminidases |
| Reactome | 14 pathways, smallest: Defective NEU1 causes sialidosis; Diseases associated with N-glycosylation of proteins; Glycosphingolipid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99519](https://www.uniprot.org/uniprotkb/Q99519) (Sialidase-1):

> Lysosomal exo-alpha-sialidase that catalyzes the removal of sialic acid (N-acetylneuraminic acid) moieties from glycoproteins and glycolipids. To be active, it is strictly dependent on its presence in the multienzyme complex. Appears to have a preference for alpha 2-3 and alpha 2-6 sialyl linkage.

**Summary**, from NCBI Gene [4758](https://www.ncbi.nlm.nih.gov/gene/4758):

> The protein encoded by this gene is a lysosomal enzyme that cleaves terminal sialic acid residues from substrates such as glycoproteins and glycolipids. In the lysosome, this enzyme is part of a heterotrimeric complex together with beta-galactosidase and cathepsin A (the latter is also referred to as 'protective protein'). Mutations in this gene can lead to sialidosis, a lysosomal storage disease that can be type 1 (cherry red spot-myoclonus syndrome or normosomatic type), which is late-onset, …

**Accessions** — [HGNC:7758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7758) · Entrez [4758](https://www.ncbi.nlm.nih.gov/gene/4758) · UniProt [Q99519](https://www.uniprot.org/uniprotkb/Q99519) · Ensembl [ENSG00000204386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204386)

## Data

Gene col 12863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12863); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12863]; `tensor/DDL_lfc|DDL_z.npy` [12863]; `embed/gene_vectors.npy` [12863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12863 or target_col == 12863). Every well: [[NEU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
