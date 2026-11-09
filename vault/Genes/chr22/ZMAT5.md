---
symbol: "ZMAT5"
type: "gene"
col: 1924
ensembl_id: "ENSG00000100319"
name: "zinc finger matrin-type 5"
location: "22q12.2"
module: 79
arm: "+"
pooled_cpm: 7.5
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ZMAT5

*zinc finger matrin-type 5* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +16.8, q 0e+00, up in 38 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Macitentan (drug)]] 5 µM in 1 line (A-172 0.0794×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.102×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF122]] (+0.69, fdr 1e-05), [[NARF]] (+0.63, fdr 2e-05), [[LMBR1L]] (+0.62, fdr 5e-05); moves opposite to [[FARSB]] (-0.68, fdr 1e-05), [[LAS1L]] (-0.64, fdr 3e-05), [[HNRNPD]] (-0.63, fdr 4e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[UBR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +16.8 | 0e+00 | 38/41 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +12.1 | 3e-31 | 43/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +11.7 | 2e-29 | 43/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +8.8 | 2e-16 | 33/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +8.1 | 6e-14 | 28/45 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.1 | 1e-10 | 22/41 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.6 | 3e-09 | 22/42 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.8 | 6e-07 | 22/38 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 2e-06 | 21/46 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 13/48 (NCI-H1573, HCT15, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 8e-04 | 14/48 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.2 | 0.001 | 2/48 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +4.2 | 0.001 | 10/47 (SW1417, LoVo, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.0 | 0.003 | 7/31 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.34×** | +3.9 | 0.003 | 16/44 (LoVo, SW1417, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.019 | 13/46 (LoVo, HOP62, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.034 | 8/45 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.045 | 6/44 (RKO, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.057 | 5/43 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.057 | 8/40 (NCI-H1792, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Macitentan (drug)]] 5 µM in 1 line (A-172 0.0794×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.102×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.5 µM 0.102× (z -9.7) |
| [[A-172 (line)]] | wt | 4.94 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0794× (z -10.0) |
| [[KATO III (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 6.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[SW480 (line)]] | alt | 7.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.8) | — |
| [[A-427 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF122]] | +0.69 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[NARF]] | +0.63 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LMBR1L]] | +0.62 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[FAM53C]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[RAB40C]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[KDM2A]] | +0.61 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[DEDD2]] | +0.61 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[UBE2O]] | +0.60 | +0.29 / +0.76 | both halves | 3e-04 |  |
| [[COG7]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RABAC1]] | +0.58 | +0.28 / +0.61 | both halves | 3e-04 |  |
| [[VPS37D]] | +0.57 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[SAP30-DT]] | +0.57 | +0.37 / +0.63 | both halves | 9e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | -0.68 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[LAS1L]] | -0.64 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[HNRNPD]] | -0.63 | -0.43 / -0.66 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[IPO9]] | -0.63 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[SRSF10]] | -0.60 | -0.35 / -0.61 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[GNL3L]] | -0.59 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[NAA15]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[TFDP1]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ATIC]] | -0.57 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[ANAPC7]] | -0.57 | -0.23 / -0.66 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBR2]] | C | ZMAT5's natural level weakens UBR2's drug response | ZMAT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.35; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.9, -34.5); signed map (-30.7, 24.9). **Vector** length 53.7, 7.12% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +16.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.2 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger matrin-type 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,730,956-29,767,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNRNP20; previously ZC3H19 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Zinc fingers matrin-type; U11/U12 di-snRNP |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q9UDW3](https://www.uniprot.org/uniprotkb/Q9UDW3) carries no function annotation.

**Summary**, from NCBI Gene [55954](https://www.ncbi.nlm.nih.gov/gene/55954):

> Predicted to enable zinc ion binding activity. Predicted to be involved in spliceosome conformational change to release U4 (or U4atac) and U1 (or U11). Located in nucleoplasm. Part of U12-type spliceosomal complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28046) · Entrez [55954](https://www.ncbi.nlm.nih.gov/gene/55954) · UniProt [Q9UDW3](https://www.uniprot.org/uniprotkb/Q9UDW3) · Ensembl [ENSG00000100319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100319)

## Data

Gene col 1924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1924); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1924]; `tensor/DDL_lfc|DDL_z.npy` [1924]; `embed/gene_vectors.npy` [1924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1924 or target_col == 1924). Every well: [[ZMAT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMAT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
