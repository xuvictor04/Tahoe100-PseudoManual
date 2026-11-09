---
symbol: "TMF1"
type: "gene"
col: 6925
ensembl_id: "ENSG00000144747"
name: "TATA element modulatory factor 1"
location: "3p14.1"
module: 41
arm: "+"
pooled_cpm: 244.06
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TMF1

*TATA element modulatory factor 1* — 3p14.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.19×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.650× (z -8.0, q 9e-13, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.759× (z -6.4, q 1e-08, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2]] (+0.83, fdr 7e-06), [[SPTY2D1]] (+0.80, fdr 7e-06), [[GOLGA4]] (+0.76, fdr 7e-06); moves opposite to [[VMA21]] (-0.61, fdr 1e-05), [[WDR77]] (-0.59, fdr 1e-05), [[NUDT3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.19×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.5 | 0.31 | 10/48 (LS 180, C32, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.13× | +3.0 | 0.68 | 5/49 (Panc 03.27, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.650×** | -8.0 | 9e-13 | 42/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.727×** | -7.5 | 1e-11 | 37/49 (A498, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.662×** | -7.3 | 4e-11 | 33/44 (AsPC-1, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.682×** | -7.1 | 2e-10 | 34/49 (AsPC-1, SW 900, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.672×** | -6.8 | 1e-09 | 36/45 (hTERT-HPNE, KATO III, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -6.4 | 1e-08 | 43/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.706×** | -6.4 | 1e-08 | 35/48 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.721×** | -6.0 | 1e-07 | 28/48 (SW 900, AsPC-1, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.7 | 9e-07 | 32/48 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.747×** | -5.4 | 4e-06 | 39/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.755×** | -5.0 | 3e-05 | 37/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.761×** | -4.8 | 6e-05 | 33/48 (HS-578T, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -4.6 | 2e-04 | 32/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.779×** | -4.4 | 4e-04 | 29/47 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.792×** | -4.1 | 0.001 | 27/50 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.803×** | -3.8 | 0.004 | 28/47 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.817×** | -3.7 | 0.006 | 24/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.010 | 26/49 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.011 | 27/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.724×** | -3.1 | 0.041 | 21/48 (NCI-H2347, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.041 | 21/48 (A-172, J82, …) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | 0.882× | -3.1 | 0.041 | 4/48 (Hs 766T, CHP-212, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.872× | -3.1 | 0.041 | 6/48 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.046 | 18/48 (SHP-77, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.046 | 17/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -2.9 | 0.062 | 13/48 (H4, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 472 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.582× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 335 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 264 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.591× (z -8.8) |
| [[H4 (line)]] | wt | 231 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 328 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 308 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.527× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 323 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 288 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.495× (z -9.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 219 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -9.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 235 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.509× (z -9.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 343 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 282 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.517× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.239× (z -9.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 393 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.602× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 189 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 228 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 229 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 196 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 272 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 211 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 283 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 262 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | same gene group |
| [[SPTY2D1]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA4]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 795 |
| [[UFL1]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.75 | +0.77 / +0.67 | both halves | 7e-06 | same gene group; STRING 564 |
| [[ACBD3]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[SRP54]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZRSR2]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TBC1D8B]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[WDR77]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[NUDT3]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PRRC2B]] | -0.57 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.4, -38.2); signed map (-50.4, 15.5). **Vector** length 148, 55.6% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.54 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 8); *Intra-Golgi traffic* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.9 | +2.0 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -6.4 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -5.8 | -6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.4 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | TATA element modulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:69,019,827-69,052,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARA160, TMF |
| Gene groups (HGNC) | Golgins; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P82094](https://www.uniprot.org/uniprotkb/P82094) (TATA element modulatory factor):

> Potential coactivator of the androgen receptor. Mediates STAT3 degradation. May play critical roles in two RAB6-dependent retrograde transport processes: one from endosomes to the Golgi and the other from the Golgi to the ER. This protein binds the HIV-1 TATA element and inhibits transcriptional activation by the TATA-binding protein (TBP).

**Summary**, from NCBI Gene [7110](https://www.ncbi.nlm.nih.gov/gene/7110):

> Enables nuclear androgen receptor binding activity and transcription coactivator activity. Involved in androgen receptor signaling pathway and positive regulation of transcription by RNA polymerase II. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11870) · Entrez [7110](https://www.ncbi.nlm.nih.gov/gene/7110) · UniProt [P82094](https://www.uniprot.org/uniprotkb/P82094) · Ensembl [ENSG00000144747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144747)

## Data

Gene col 6925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6925); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6925]; `tensor/DDL_lfc|DDL_z.npy` [6925]; `embed/gene_vectors.npy` [6925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6925 or target_col == 6925). Every well: [[TMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
