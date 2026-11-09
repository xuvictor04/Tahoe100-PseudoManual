---
symbol: "GCNA"
type: "gene"
col: 7160
ensembl_id: "ENSG00000147174"
name: "germ cell nuclear acidic peptidase"
location: "Xq13.1"
module: 39
arm: "+"
pooled_cpm: 21.95
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GCNA

*germ cell nuclear acidic peptidase* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +7.1, q 9e-10, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.429× (z -8.9, q 2e-16, down in 32 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.459× (z -8.2, q 5e-14, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.80, fdr 7e-06), [[MYOCOS]] (+0.77, fdr 7e-06), [[LINC02936]] (+0.77, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +7.1 | 9e-10 | 30/47 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.0 | 7e-07 | 30/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.8 | 1e-06 | 23/44 (NCI-H2030, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.72×** | +5.7 | 2e-06 | 34/48 (SW480, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.1 | 3e-05 | 27/48 (SHP-77, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.0 | 4e-05 | 26/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 4e-05 | 22/44 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.043 | 19/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Naproxen (drug)]] 0.05 µM |  | 1.37× | +3.0 | 0.14 | 14/45 (H4, CHP-212, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.0 | 0.14 | 15/42 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -8.9 | 2e-16 | 32/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.459×** | -8.2 | 5e-14 | 34/45 (PANC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -7.3 | 5e-11 | 34/48 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.507×** | -7.2 | 9e-11 | 30/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -5.6 | 2e-06 | 27/47 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.596×** | -5.5 | 4e-06 | 26/48 (PANC-1, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.640×** | -4.7 | 2e-04 | 26/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -4.4 | 6e-04 | 21/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.655×** | -4.2 | 0.002 | 22/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.9 | 0.005 | 23/48 (PANC-1, KATO III, …) | all doses, flat | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.710×** | -3.5 | 0.025 | 18/48 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift |
| [[NG25 (drug)]] 5 µM |  | **0.541×** | -3.4 | 0.032 | 17/44 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.043 | 14/47 (C-33 A, SW48, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.734×** | -3.3 | 0.043 | 14/48 (HT-29, PANC-1, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.555×** | -3.3 | 0.043 | 14/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -15.7) |
| [[KATO III (line)]] | alt | 40.0 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -11.6) |
| [[H4 (line)]] | wt | 35.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0749× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -12.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.7 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[BT-474 (line)]] | alt | 19.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +10.2) | [[Cobimetinib (drug)]] 5 µM 0.136× (z -9.2) |
| [[HOP62 (line)]] | alt | 22.8 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 50.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.97× (z +10.2) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0986× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 72.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 21.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +16.1) | [[Bosentan (hydrate) (drug)]] 5 µM 0.153× (z -9.5) |
| [[SW48 (line)]] | wt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +9.7) | — |
| [[A-172 (line)]] | wt | 17.2 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.107× (z -10.0) |
| [[A549 (line)]] | wt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.121× (z -8.8) |
| [[C32 (line)]] | wt | 7.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0936× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 8.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.318× (z -8.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SHP-77 (line)]] | alt | 6.86 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0559× (z -10.6) |
| [[SNU-1 (line)]] | wt | 9.75 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0775× (z -8.8) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.80 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.77 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.77 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.76 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[MSH4]] | +0.76 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.75 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GCNA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IMPA1P1]] | B | IMPA1P1 activity raises GCNA's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without IMPA1P1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises GCNA's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without C21orf91-OT1 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[TOP2B]] | B | TOP2B activity lowers GCNA's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.8, -15.2); signed map (15.7, 7.9). **Vector** length 125, 33.8% of its response variance represented; |z| ≥ 3 in 1,313 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +6.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.4 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.7 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | germ cell nuclear acidic peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,578,437-71,613,583 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAAR1; previously ACRC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QF7](https://www.uniprot.org/uniprotkb/Q96QF7) (Germ cell nuclear acidic protein):

> May play a role in DNA-protein cross-links (DPCs) clearance through a SUMO-dependent recruitment to sites of DPCs, ensuring the genomic stability by protecting germ cells and early embryos from various sources of damage. Can resolve the topoisomerase II (TOP2A) DPCs (By similarity).

**Summary**, from NCBI Gene [93953](https://www.ncbi.nlm.nih.gov/gene/93953):

> Enables SUMO polymer binding activity. Involved in protein-DNA covalent cross-linking repair. Located in PML body. Implicated in X-linked spermatogenic failure 4. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15805) · Entrez [93953](https://www.ncbi.nlm.nih.gov/gene/93953) · UniProt [Q96QF7](https://www.uniprot.org/uniprotkb/Q96QF7) · Ensembl [ENSG00000147174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147174)

## Data

Gene col 7160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7160); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7160]; `tensor/DDL_lfc|DDL_z.npy` [7160]; `embed/gene_vectors.npy` [7160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7160 or target_col == 7160). Every well: [[GCNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
