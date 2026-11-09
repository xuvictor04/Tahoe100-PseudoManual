---
symbol: "PARP2"
type: "gene"
col: 4979
ensembl_id: "ENSG00000129484"
name: "poly(ADP-ribose) polymerase 2"
location: "14q11.2"
module: 17
arm: "+"
pooled_cpm: 32.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PARP2

*poly(ADP-ribose) polymerase 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.76× (z +4.8, q 1e-03, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.26× (z +3.8, q 0.018, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -13.6, q 1e-39, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH11]] (+0.72, fdr 7e-06), [[CEP192]] (+0.67, fdr 7e-06), [[SASS6]] (+0.65, fdr 7e-06); moves opposite to [[HCG17]] (-0.59, fdr 5e-05), [[CASC11]] (-0.56, fdr 3e-05), [[GNG12-AS1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +4.8 | 1e-03 | 25/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.33×** | +4.5 | 0.001 | 22/48 (RKO, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.5 | 0.001 | 21/48 (NCI-H23, LS 180, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.1 | 0.006 | 22/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.018 | 17/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.024 | 11/47 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **1.24×** | +3.5 | 0.044 | 18/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.4 | 0.050 | 21/48 (NCI-H1573, C-33 A, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.055 | 11/48 (RKO, SNU-1, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.059 | 12/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.078 | 13/47 (HT-29, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -13.6 | 1e-39 | 43/48 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.776×** | -5.7 | 3e-06 | 25/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.793×** | -5.2 | 3e-05 | 23/48 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.8 | 3e-04 | 25/47 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -4.5 | 8e-04 | 1/48 (SW 900) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.4 | 0.001 | 24/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.760×** | -4.1 | 0.003 | 18/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.837× | -4.0 | 0.004 | 11/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.788×** | -3.8 | 0.009 | 19/47 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.720×** | -3.7 | 0.010 | 15/48 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.653×** | -3.6 | 0.019 | 8/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.809×** | -3.4 | 0.034 | 11/47 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.675×** | -3.3 | 0.045 | 9/48 (H4, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.817×** | -3.2 | 0.052 | 15/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.823×** | -3.1 | 0.072 | 11/48 (MIA PaCa-2, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.828×** | -3.0 | 0.087 | 11/47 (COLO 205, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 23.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0618× (z -13.9) |
| [[C-33 A (line)]] | alt | 67.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 44.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.9) |
| [[A498 (line)]] | wt | 38.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.7) |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0732× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 38.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.6) |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.4) |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0881× (z -8.8) |
| [[J82 (line)]] | alt | 33.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.9) |
| [[LS 180 (line)]] | wt | 37.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -8.5) |
| [[RKO (line)]] | wt | 39.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -12.4) |
| [[SW480 (line)]] | alt | 30.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.8) |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | +0.72 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CEP192]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SASS6]] | +0.65 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[POT1]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Base Excision Repair |
| [[CEP57L1]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[RFC1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 | pathway: Base Excision Repair |
| [[EXOSC9]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FIGNL1]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[HPF1]] | +0.61 | +0.42 / +0.51 | both halves | 4e-05 | STRING 999 |
| [[BUD13]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MIS18A]] | +0.60 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[COMMD2]] | +0.60 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG17]] | -0.59 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[CASC11]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GNG12-AS1]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CCNT2-AS1]] | -0.56 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TAFA2]] | -0.54 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[LINC01088]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[C2orf88]] | -0.52 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[DGKH]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[BCL10-AS1]] | -0.51 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[CTTN]] | -0.51 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[BHLHE40-AS1]] | -0.51 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MKLN1-AS]] | -0.51 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PARP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-43.9, -55.4); signed map (-43.3, -35.8). **Vector** length 100, 25.4% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,343,615-20,357,904 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARTD2; previously ADPRTL2 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Hallmark sets | SPERMATOGENESIS, UV_RESPONSE_UP |
| Reactome | 13 pathways, smallest: POLB-Dependent Long Patch Base Excision Repair; HDR through MMEJ (alt-NHEJ); Resolution of AP sites via the multiple-nucleotide patch replacement pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGN5](https://www.uniprot.org/uniprotkb/Q9UGN5) (Poly):

> Poly-ADP-ribosyltransferase that mediates poly-ADP-ribosylation of proteins and plays a key role in DNA repair. Mediates glutamate, aspartate or serine ADP-ribosylation of proteins: the ADP-D-ribosyl group of NAD(+) is transferred to the acceptor carboxyl group of target residues and further ADP-ribosyl groups are transferred to the 2'-position of the terminal adenosine moiety, building up a polymer with an average chain length of 20-30 units. Serine ADP-ribosylation of proteins constitutes the …

**Summary**, from NCBI Gene [10038](https://www.ncbi.nlm.nih.gov/gene/10038):

> This gene encodes poly(ADP-ribosyl)transferase-like 2 protein, which contains a catalytic domain and is capable of catalyzing a poly(ADP-ribosyl)ation reaction. This protein has a catalytic domain which is homologous to that of poly (ADP-ribosyl) transferase, but lacks an N-terminal DNA binding domain which activates the C-terminal catalytic domain of poly (ADP-ribosyl) transferase. The basic residues within the N-terminal region of this protein may bear potential DNA-binding properties, and …

**Accessions** — [HGNC:272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:272) · Entrez [10038](https://www.ncbi.nlm.nih.gov/gene/10038) · UniProt [Q9UGN5](https://www.uniprot.org/uniprotkb/Q9UGN5) · Ensembl [ENSG00000129484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129484)

## Data

Gene col 4979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4979); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4979]; `tensor/DDL_lfc|DDL_z.npy` [4979]; `embed/gene_vectors.npy` [4979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4979 or target_col == 4979). Every well: [[PARP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
