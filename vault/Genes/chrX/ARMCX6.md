---
symbol: "ARMCX6"
type: "gene"
col: 12757
ensembl_id: "ENSG00000198960"
name: "armadillo repeat containing X-linked 6"
location: "Xq22.1"
module: 178
arm: "+"
pooled_cpm: 2.73
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# ARMCX6

*armadillo repeat containing X-linked 6* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.52× (z +5.9, q 2e-06, up in 6 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.565× (z -5.7, q 8e-06, down in 18 of 39 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.696× (z -3.6, q 0.032, down in 11 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH9P]] (+0.54, fdr 2e-05), [[ZNF224]] (+0.52, fdr 8e-05), [[LMAN2L]] (+0.52, fdr 3e-05); moves opposite to [[HOMER1]] (-0.53, fdr 1e-05), [[H3-3B]] (-0.49, fdr 5e-05), [[PHLDA2]] (-0.48, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNK15-AS1]] → it (grade B ⚠); 7 go from it, the strongest it → [[WASH9P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +5.9 | 2e-06 | 6/40 (NCI-H460, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +4.6 | 0.001 | 10/35 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.1 | 0.007 | 1/15 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +4.1 | 0.007 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.4 | 0.066 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.3 | 0.087 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.2 | 0.11 | 0/20 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.35× | +3.0 | 0.19 | 1/42 (J82) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.565×** | -5.7 | 8e-06 | 18/39 (C32, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.576×** | -5.5 | 1e-05 | 15/39 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.634×** | -4.5 | 0.001 | 13/41 (KATO III, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.634×** | -4.4 | 0.002 | 8/25 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.032 | 11/39 (C32, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.697×** | -3.6 | 0.032 | 11/40 (AN3 CA, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.4 | 0.060 | 13/32 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **0.695×** | -3.3 | 0.060 | 7/32 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.723× | -3.1 | 0.12 | 8/40 (Panc 03.27, HCT15, …) | top dose only | composition shift; position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.725× | -3.1 | 0.13 | 2/40 (SW480, A-427) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.45 | 0 | 2 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0603× (z -9.1) |
| [[A-172 (line)]] | wt | 2.75 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0600× (z -8.6) |
| [[A498 (line)]] | wt | 3.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -8.9) |
| [[SNU-423 (line)]] | alt | 3.62 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0618× (z -8.7) |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.815 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH9P]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZNF224]] | +0.52 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[LMAN2L]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[EIF4B]] | +0.51 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[ZBTB26]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[TIGD1]] | +0.50 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[ZNF383]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ZNF221]] | +0.49 | +0.21 / +0.56 | both halves | 6e-04 |  |
| [[TMEM94]] | +0.49 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[ZSCAN25]] | +0.48 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PECR]] | +0.48 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ZNF775]] | +0.48 | +0.42 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMER1]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.49 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PHLDA2]] | -0.48 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MFSD2A]] | -0.48 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ADARB1]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MYO1E]] | -0.45 | -0.24 / -0.47 | both halves | 5e-04 |  |
| [[RCOR1]] | -0.45 | -0.26 / -0.38 | both halves | 3e-04 |  |
| [[SERTAD1]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MARCHF3]] | -0.45 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[PITPNC1]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[SLC9A1]] | -0.44 | -0.40 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK15-AS1]] | B | KCNK15-AS1 activity raises ARMCX6's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without KCNK15-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[ZNF790]] | B | ZNF790 activity raises ARMCX6's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without ZNF790 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |
| [[HDAC6]] | B | HDAC6 activity raises ARMCX6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WASH9P]] | C | ARMCX6 activity lowers WASH9P's level | lines that do not express ARMCX6 (3) vs lines expressing it (46) | 1.43× higher at baseline in the lines without ARMCX6 | 0.064 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | ARMCX6 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express ARMCX6 (3) vs lines expressing it (44) | the lines without ARMCX6: 0.78× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ARMCX6 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ARMCX6 (3) vs lines expressing it (44) | the lines without ARMCX6: 1.36× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| [[SNHG22]] | C | ARMCX6 activity lowers SNHG22's level | lines that do not express ARMCX6 (3) vs lines expressing it (46) | 2.05× higher at baseline in the lines without ARMCX6 | 0.083 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| [[ZNF223]] | C | ARMCX6 activity raises ZNF223's level | lines that do not express ARMCX6 (3) vs lines expressing it (46) | 3.10× lower at baseline in the lines without ARMCX6 | 0.086 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| cells under [[Docetaxel (drug)]] 0.05 µM | C | ARMCX6 activity lowers the cells' numbers under Docetaxel 0.05 µM (makes them more sensitive) | lines that do not express ARMCX6 (3) vs lines expressing it (44) | the lines without ARMCX6: 1.87× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | ARMCX6 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express ARMCX6 (3) vs lines expressing it (44) | the lines without ARMCX6: 0.74× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.6, 19.2); signed map (-12.6, -18.3). **Vector** length 38.2, 4.03% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.1 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.1 | -3.1 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.1 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Malotilate (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,615,118-101,618,001 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20811, GASP10 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L4S7](https://www.uniprot.org/uniprotkb/Q7L4S7) (Protein ARMCX6):

> May regulate the dynamics and distribution of mitochondria in neural cells.

**Summary**, from NCBI Gene [54470](https://www.ncbi.nlm.nih.gov/gene/54470):

> Predicted to be involved in axonal transport of mitochondrion. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26094) · Entrez [54470](https://www.ncbi.nlm.nih.gov/gene/54470) · UniProt [Q7L4S7](https://www.uniprot.org/uniprotkb/Q7L4S7) · Ensembl [ENSG00000198960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198960)

## Data

Gene col 12757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12757); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12757]; `tensor/DDL_lfc|DDL_z.npy` [12757]; `embed/gene_vectors.npy` [12757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12757 or target_col == 12757). Every well: [[ARMCX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
