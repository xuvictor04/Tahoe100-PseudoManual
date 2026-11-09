---
symbol: "PURA"
type: "gene"
col: 11631
ensembl_id: "ENSG00000185129"
name: "purine rich element binding protein A"
location: "5q31.3"
module: 20
arm: "-"
pooled_cpm: 86.6
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PURA

*purine rich element binding protein A* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.32× (z +4.0, q 0.031, up in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 4 lines (LOX-IMVI 3.88×, A-172 2.69×, HOP62 2.46×, SNU-423 2.54×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 2.66×, A498 2.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 2.47×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.477× (z -10.8, q 2e-24, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGIP]] (+0.83, fdr 7e-06, ⚠ same locus), [[TERF2IP]] (+0.70, fdr 7e-06), [[ING2]] (+0.69, fdr 1e-05), [[FUT11]] (+0.68, fdr 3e-05); moves opposite to [[RPSA]] (-0.64, fdr 7e-06), [[YWHAQ]] (-0.63, fdr 7e-06), [[EFTUD2]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IGIP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 4 lines (LOX-IMVI 3.88×, A-172 2.69×, HOP62 2.46×, SNU-423 2.54×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 2.66×, A498 2.02×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 2.47×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.031 | 33/49 (HOP62, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.044 | 25/47 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.044 | 21/49 (A549, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.099 | 27/48 (KATO III, AN3 CA, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.3 | 0.10 | 27/48 (KATO III, NCI-H1573, …) | all doses, flat |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.16× | +3.2 | 0.13 | 9/49 (A498, SNU-1, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.14 | 24/49 (BT-474, CHP-212, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.23× | +3.1 | 0.14 | 22/48 (Hs 766T, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -10.8 | 2e-24 | 45/48 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.537×** | -8.6 | 3e-15 | 44/48 (HT-29, HCT15, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -8.5 | 4e-15 | 41/48 (HT-29, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -7.3 | 4e-11 | 46/49 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -6.4 | 1e-08 | 38/48 (HOP62, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -6.2 | 5e-08 | 33/48 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -6.0 | 2e-07 | 36/48 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.5 | 5e-04 | 30/47 (HCT15, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -4.4 | 6e-04 | 27/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.4 | 6e-04 | 28/45 (SW48, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -4.0 | 0.004 | 28/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -3.9 | 0.005 | 20/37 (HS-578T, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.792×** | -3.4 | 0.031 | 24/48 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.035 | 24/48 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.043 | 23/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 116 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.46× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.2) |
| [[HCT15 (line)]] | alt | 138 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -13.8) |
| [[HS-578T (line)]] | alt | 109 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.442× (z -9.9) |
| [[HT-29 (line)]] | alt | 97.4 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -14.4) |
| [[LoVo (line)]] | wt | 139 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -11.0) |
| [[H4 (line)]] | wt | 97.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -11.5) |
| [[KATO III (line)]] | alt | 96.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.437× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 151 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.88× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.3) |
| [[LS 180 (line)]] | wt | 76.2 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.370× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 71.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -8.7) |
| [[SNU-423 (line)]] | alt | 101 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.54× (z +10.2) | [[Bortezomib (drug)]] 0.05 µM 0.431× (z -8.6) |
| [[A-172 (line)]] | wt | 101 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +10.8) | — |
| [[A498 (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 84.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -9.5) |
| [[COLO 205 (line)]] | alt | 137 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.326× (z -10.5) |
| [[Hs 766T (line)]] | wt | 123 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 46.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.351× (z -9.7) |
| [[NCI-H596 (line)]] | alt | 87.2 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[PANC-1 (line)]] | alt | 99.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.446× (z -10.8) |
| [[SW1417 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.47× (z +9.5) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 78.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGIP]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.3 kb, same strand: neighbours can correlate without regulation) |
| [[TERF2IP]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ING2]] | +0.69 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[FUT11]] | +0.68 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[NR2F2]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[RSBN1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TMF1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[FOXA2]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[NKAP]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[SAP30]] | +0.61 | +0.46 / +0.70 | both halves | 3e-05 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.63 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.62 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[DARS2]] | -0.60 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.60 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[NIT2]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PSME3]] | -0.59 | -0.46 / -0.68 | both halves | 2e-05 |  |
| [[PRPS1]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TCP1]] | -0.58 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[WDR77]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGIP]] | C | IGIP's natural level strengthens PURA's drug response | IGIP's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.57; direction not clear | 1e-03 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.3, -30.7); signed map (-6.6, 5.6). **Vector** length 112, 35.5% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.8 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.1 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.4 | -10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -8.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | purine rich element binding protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,107,777-140,125,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PURALPHA, PUR1, PUR-ALPHA |
| Gene groups (HGNC) | Purine rich element binding protein family |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00577](https://www.uniprot.org/uniprotkb/Q00577) (Transcriptional activator protein Pur-alpha):

> This is a probable transcription activator that specifically binds the purine-rich single strand of the PUR element located upstream of the MYC gene. May play a role in the initiation of DNA replication and in recombination.

**Summary**, from NCBI Gene [5813](https://www.ncbi.nlm.nih.gov/gene/5813):

> This gene product is a sequence-specific, single-stranded DNA-binding protein. It binds preferentially to the single strand of the purine-rich element termed PUR, which is present at origins of replication and in gene flanking regions in a variety of eukaryotes from yeasts through humans. Thus, it is implicated in the control of both DNA replication and transcription. Deletion of this gene has been associated with myelodysplastic syndrome and acute myelogenous leukemia. [provided by RefSeq, Jul …

**Accessions** — [HGNC:9701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9701) · Entrez [5813](https://www.ncbi.nlm.nih.gov/gene/5813) · UniProt [Q00577](https://www.uniprot.org/uniprotkb/Q00577) · Ensembl [ENSG00000185129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185129)

## Data

Gene col 11631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11631); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11631]; `tensor/DDL_lfc|DDL_z.npy` [11631]; `embed/gene_vectors.npy` [11631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11631 or target_col == 11631). Every well: [[PURA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PURA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
