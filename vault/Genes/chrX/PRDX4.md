---
symbol: "PRDX4"
type: "gene"
col: 4405
ensembl_id: "ENSG00000123131"
name: "peroxiredoxin 4"
location: "Xp22.11"
module: 48
arm: "+"
pooled_cpm: 45.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PRDX4

*peroxiredoxin 4* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.48× (z +8.9, q 2e-16, up in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +4.3, q 0.002, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 4.71×, KATO III 3.55×, LoVo 3.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 4.51×, NCI-H1573 4.53×, A-427 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.281× (z -17.7, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR4]] (+0.68, fdr 7e-06), [[VKORC1]] (+0.67, fdr 7e-06), [[POM121]] (+0.65, fdr 1e-05); moves opposite to [[BCL7B]] (-0.64, fdr 1e-05), [[C22orf46]] (-0.57, fdr 1e-05), [[PSMD6]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 4.71×, KATO III 3.55×, LoVo 3.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 4.51×, NCI-H1573 4.53×, A-427 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.48×** | +8.9 | 2e-16 | 40/45 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.01×** | +6.6 | 1e-08 | 34/39 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.59×** | +4.6 | 1e-03 | 32/47 (NCI-H1573, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 31/48 (SNU-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +4.1 | 0.004 | 28/44 (KATO III, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.45×** | +3.6 | 0.027 | 27/47 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.039 | 26/46 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.083 | 31/48 (NCI-H2347, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.281×** | -17.7 | 0e+00 | 47/47 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.438×** | -8.1 | 1e-13 | 38/47 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -6.2 | 9e-08 | 41/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.653×** | -4.2 | 0.004 | 33/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -4.0 | 0.007 | 31/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.653×** | -3.8 | 0.013 | 30/48 (C32, HCT15, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.059 | 27/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.13 | 22/48 (HEC-1-A, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 71.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.4) |
| [[A-427 (line)]] | wt | 51.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -20.8) |
| [[KATO III (line)]] | alt | 67.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.0) |
| [[LoVo (line)]] | wt | 25.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.8) |
| [[A498 (line)]] | wt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.1) |
| [[A549 (line)]] | wt | 49.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 39.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.6) |
| [[HS-578T (line)]] | alt | 66.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 82.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 60.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.4) |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.1) |
| [[BT-474 (line)]] | alt | 52.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.5) |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.8) |
| [[C32 (line)]] | wt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.8) |
| [[H4 (line)]] | wt | 66.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.1) |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.0) |
| [[HOP62 (line)]] | alt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.2) |
| [[Hs 766T (line)]] | wt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.8) |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.9) |
| [[J82 (line)]] | alt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.0) |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 55.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) |
| [[PANC-1 (line)]] | alt | 40.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.8) |
| [[RKO (line)]] | wt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[SNU-1 (line)]] | wt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -16.7) |
| [[SNU-423 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.3) |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.0) |
| [[SW1417 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.4) |
| [[SW480 (line)]] | alt | 46.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -18.1) |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR4]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 | STRING 531 |
| [[VKORC1]] | +0.67 | +0.67 / +0.74 | both halves | 7e-06 | STRING 543 |
| [[POM121]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[PRELID1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[OST4]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MIF]] | +0.65 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[CD320]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ATP6AP2]] | +0.62 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[UBL5]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PPIB]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.60 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7B]] | -0.64 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[C22orf46]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PSMD6]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[GAS8]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PPID]] | -0.55 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[SLC35A4]] | -0.55 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[RTL6]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TCTN1]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZKSCAN3]] | -0.54 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[MOB3C]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SRSF3]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[GRIPAP1]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PRDX4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PRDX4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-50.7, -20.6); signed map (-37.0, 11.7). **Vector** length 88.7, 29.4% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.1 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -17.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,664,262-23,686,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AOE37-2 |
| Gene groups (HGNC) | Peroxiredoxins |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13162](https://www.uniprot.org/uniprotkb/Q13162) (Peroxiredoxin-4):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. Regulates the activation of NF-kappa-B in the cytosol by a modulation of I-kappa-B-alpha phosphorylation.

**Summary**, from NCBI Gene [10549](https://www.ncbi.nlm.nih.gov/gene/10549):

> The protein encoded by this gene is an antioxidant enzyme and belongs to the peroxiredoxin family. The protein is localized to the cytoplasm. Peroxidases of the peroxiredoxin family reduce hydrogen peroxide and alkyl hydroperoxides to water and alcohol with the use of reducing equivalents derived from thiol-containing donor molecules. This protein has been found to play a regulatory role in the activation of the transcription factor NF-kappaB. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17169) · Entrez [10549](https://www.ncbi.nlm.nih.gov/gene/10549) · UniProt [Q13162](https://www.uniprot.org/uniprotkb/Q13162) · Ensembl [ENSG00000123131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123131)

## Data

Gene col 4405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4405); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4405]; `tensor/DDL_lfc|DDL_z.npy` [4405]; `embed/gene_vectors.npy` [4405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4405 or target_col == 4405). Every well: [[PRDX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
