---
symbol: "GOLT1B"
type: "gene"
col: 3267
ensembl_id: "ENSG00000111711"
name: "golgi transport 1B"
location: "12p12.1"
module: 56
arm: "+"
pooled_cpm: 132.28
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# GOLT1B

*golgi transport 1B* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.84× (z +4.5, q 0.005, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.26×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.63×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.537× (z -12.1, q 9e-31, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER3IP1]] (+0.79, fdr 7e-06), [[GPR107]] (+0.78, fdr 7e-06), [[SLC39A7]] (+0.77, fdr 7e-06); moves opposite to [[REPIN1]] (-0.63, fdr 7e-06), [[ZNF480]] (-0.63, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEC13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.26×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.63×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +4.5 | 0.005 | 31/48 (hTERT-HPNE, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.1 | 0.011 | 30/45 (SNU-423, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.045 | 0/50 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.097 | 22/49 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.097 | 20/49 (RPMI-7951, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.537×** | -12.1 | 9e-31 | 40/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -9.2 | 8e-18 | 43/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -8.0 | 2e-13 | 39/48 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.713×** | -6.6 | 7e-09 | 41/48 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -5.9 | 5e-07 | 31/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.706×** | -4.9 | 1e-04 | 28/49 (RPMI-7951, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -4.8 | 2e-04 | 30/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -4.7 | 2e-04 | 32/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -4.6 | 2e-04 | 30/48 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -4.4 | 5e-04 | 33/48 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.724×** | -4.3 | 7e-04 | 33/48 (J82, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.742×** | -4.2 | 0.001 | 28/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.749×** | -4.0 | 0.002 | 26/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -3.9 | 0.004 | 26/44 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -3.8 | 0.005 | 22/48 (RPMI-7951, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.767×** | -3.7 | 0.007 | 26/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.007 | 26/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.781×** | -3.5 | 0.017 | 31/49 (SW1417, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 111 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -15.2) |
| [[A498 (line)]] | wt | 202 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.1) |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.9) |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.8) |
| [[HS-578T (line)]] | alt | 194 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.8) |
| [[H4 (line)]] | wt | 182 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.3) |
| [[HOP62 (line)]] | alt | 199 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 51.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.6) |
| [[SNU-1 (line)]] | wt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.7) |
| [[SW1417 (line)]] | alt | 133 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.0) |
| [[A-427 (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -8.6) |
| [[HCT15 (line)]] | alt | 133 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0495× (z -11.2) |
| [[Hs 766T (line)]] | wt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.8) |
| [[HT-29 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.7) |
| [[J82 (line)]] | alt | 196 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.1) |
| [[LoVo (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.4) |
| [[RKO (line)]] | wt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 96.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.0) |
| [[SW 1271 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.8) |
| [[SW48 (line)]] | wt | 96.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.3) |
| [[A549 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 119 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER3IP1]] | +0.79 | +0.85 / +0.78 | both halves | 7e-06 | STRING 434 |
| [[GPR107]] | +0.78 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[SLC39A7]] | +0.77 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.77 | +0.87 / +0.69 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.76 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[COPA]] | +0.75 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[OSTC]] | +0.75 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.74 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[SURF4]] | +0.73 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[COG6]] | +0.73 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[PGM3]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.73 | +0.78 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REPIN1]] | -0.63 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ZNF480]] | -0.63 | -0.65 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC13]] | C | SEC13's natural level strengthens GOLT1B's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.23; direction not clear | 0.028 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, -32.0); signed map (-49.8, 9.4). **Vector** length 133, 47.7% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.63 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.65 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.65 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +11.7 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.1 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.3 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | golgi transport 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,501,781-21,518,408 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-141, YMR292W, GOT1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3E0](https://www.uniprot.org/uniprotkb/Q9Y3E0) (Vesicle transport protein GOT1B):

> May be involved in fusion of ER-derived transport vesicles with the Golgi complex.

**Summary**, from NCBI Gene [51026](https://www.ncbi.nlm.nih.gov/gene/51026):

> Involved in positive regulation of canonical NF-kappaB signal transduction. Located in endoplasmic reticulum. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20175) · Entrez [51026](https://www.ncbi.nlm.nih.gov/gene/51026) · UniProt [Q9Y3E0](https://www.uniprot.org/uniprotkb/Q9Y3E0) · Ensembl [ENSG00000111711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111711)

## Data

Gene col 3267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3267); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3267]; `tensor/DDL_lfc|DDL_z.npy` [3267]; `embed/gene_vectors.npy` [3267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3267 or target_col == 3267). Every well: [[GOLT1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLT1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
