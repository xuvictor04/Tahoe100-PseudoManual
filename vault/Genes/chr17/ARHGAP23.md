---
symbol: "ARHGAP23"
type: "gene"
col: 15860
ensembl_id: "ENSG00000275832"
name: "Rho GTPase activating protein 23"
location: "17q12"
module: 101
arm: "+"
pooled_cpm: 42.09
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ARHGAP23

*Rho GTPase activating protein 23* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +5.0, q 4e-04, up in 18 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 6.01×, A498 3.16×, RPMI-7951 4.07×, NCI-H460 3.53×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.20×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.654× (z -8.7, q 2e-15, down in 23 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO1C]] (+0.66, fdr 7e-06), [[CFAP46]] (+0.56, fdr 8e-05), [[NCOR2]] (+0.55, fdr 1e-05); moves opposite to [[HOXA5]] (-0.54, fdr 3e-05), [[HOXA6]] (-0.53, fdr 7e-05), [[NDUFAF7]] (-0.49, fdr 5e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[COL7A1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ELF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 6.01×, A498 3.16×, RPMI-7951 4.07×, NCI-H460 3.53×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.20×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.0 | 4e-04 | 18/35 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.081 | 15/36 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -8.7 | 2e-15 | 23/35 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.729×** | -6.5 | 3e-08 | 22/36 (Hs 766T, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -5.4 | 1e-05 | 22/36 (Hs 766T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -4.8 | 2e-04 | 18/36 (Hs 766T, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -4.3 | 0.002 | 18/34 (A-172, Hs 766T, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.644×** | -3.3 | 0.071 | 11/36 (LOX-IMVI, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.071 | 14/36 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.071 | 19/36 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.089 | 11/36 (HOP62, CFPAC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.737×** | -3.2 | 0.090 | 15/34 (SHP-77, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 167 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.4) | — |
| [[SW480 (line)]] | alt | 88.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.5) |
| [[A498 (line)]] | wt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 79.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.3) |
| [[HOP62 (line)]] | alt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.6) |
| [[HS-578T (line)]] | alt | 43.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.5) |
| [[HT-29 (line)]] | alt | 232 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.2) |
| [[J82 (line)]] | alt | 65.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.489× (z -9.7) |
| [[KATO III (line)]] | alt | 68.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.1) | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0959× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO1C]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CFAP46]] | +0.56 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[NCOR2]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PITPNM3]] | +0.55 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[UNC13D]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN9]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[KPNA2P3]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MEGF6]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PLCD3]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FLNC]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[MYH9]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CEP170B]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA5]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[HOXA6]] | -0.53 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[NDUFAF7]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[UQCRC2]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TVP23B]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SLC18B1]] | -0.47 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MFF]] | -0.47 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FNTB]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[FAM13A]] | -0.46 | -0.38 / -0.55 | both halves | 7e-05 | same gene group; pathway: RAC1 GTPase cycle |
| [[MED6]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[ASB7]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[COX16]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL7A1]] | B | COL7A1 activity raises ARHGAP23's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without COL7A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ARHGAP23's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF4]] | B | ARHGAP23 activity raises ELF4's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without ARHGAP23 | 0.012 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[NCOR2]] | B | ARHGAP23 activity raises NCOR2's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without ARHGAP23 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| cells under [[Belumosudil (drug)]] 5 µM | B | ARHGAP23 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ARHGAP23 (12) vs lines expressing it (36) | the lines without ARHGAP23: 0.60× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[FLNC]] | B | ARHGAP23 activity raises FLNC's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without ARHGAP23 | 0.091 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[ACTN4]] | B | ARHGAP23 activity raises ACTN4's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.63× lower at baseline in the lines without ARHGAP23 | 0.097 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.396). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, 51.8); signed map (-3.9, 33.8). **Vector** length 88.1, 21.7% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.5 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.6 | -4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,419,280-38,512,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1501 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins; PDZ domain containing |
| Reactome | 5 pathways, smallest: RHOA GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P227](https://www.uniprot.org/uniprotkb/Q9P227) (Rho GTPase-activating protein 23):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [57636](https://www.ncbi.nlm.nih.gov/gene/57636):

> The RHO (see ARHA; MIM 165390) family of small GTPases are involved in signal transduction through transmembrane receptors, and they are inactive in the GDP-bound form and active in the GTP-bound form. GTPase-activating proteins, such as ARHGAP23, inactivate RHO family proteins by stimulating their hydrolysis of GTP (Katoh and Katoh, 2004 [PubMed 15254754]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29293) · Entrez [57636](https://www.ncbi.nlm.nih.gov/gene/57636) · UniProt [Q9P227](https://www.uniprot.org/uniprotkb/Q9P227) · Ensembl [ENSG00000275832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275832)

## Data

Gene col 15860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15860); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15860]; `tensor/DDL_lfc|DDL_z.npy` [15860]; `embed/gene_vectors.npy` [15860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15860 or target_col == 15860). Every well: [[ARHGAP23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
