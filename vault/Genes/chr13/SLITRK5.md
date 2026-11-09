---
symbol: "SLITRK5"
type: "gene"
col: 9104
ensembl_id: "ENSG00000165300"
name: "SLIT and NTRK like family member 5"
location: "13q31.2"
module: 19
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 27
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLITRK5

*SLIT and NTRK like family member 5* — 13q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.85× (z +9.1, q 5e-17, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 2.16× (z +6.9, q 7e-10, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.510× (z -5.5, q 2e-05, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC63]] (+0.70, fdr 7e-06), [[SNCA]] (+0.70, fdr 7e-06), [[ZFHX4]] (+0.68, fdr 7e-06); moves opposite to [[CCL3]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02945]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[HI-TOPK-032 (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +9.1 | 5e-17 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.0 | 5e-17 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.4 | 8e-15 | 1/15 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.16×** | +6.9 | 7e-10 | 18/24 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +6.7 | 2e-09 | 13/23 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +5.7 | 1e-06 | 12/21 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.93×** | +5.5 | 3e-06 | 14/21 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.51×** | +5.3 | 9e-06 | 16/22 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.61×** | +4.3 | 0.001 | 4/21 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.89×** | +4.1 | 0.003 | 1/9 (J82) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.005 | 9/24 (J82, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.2 | 0.067 | 2/13 (NCI-H1792, SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.071 | 2/23 (COLO 205, NCI-H1573) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.0 | 0.087 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.087 | 1/17 (NCI-H2030) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.087 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -5.5 | 2e-05 | 13/22 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -5.4 | 2e-05 | 18/23 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.576×** | -4.9 | 2e-04 | 12/24 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.597×** | -4.6 | 6e-04 | 13/24 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -4.2 | 0.003 | 14/23 (A-427, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.625×** | -4.0 | 0.005 | 7/21 (NCI-H2347, HEC-1-A, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.648×** | -3.9 | 0.009 | 9/21 (AN3 CA, A549, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.655×** | -3.6 | 0.020 | 8/21 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.701×** | -3.2 | 0.098 | 8/22 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.690×** | -3.1 | 0.098 | 9/22 (NCI-H460, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -3.1 | 0.098 | 13/22 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.703× | -3.0 | 0.12 | 11/21 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 13 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0628× (z -15.7) |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -12.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.56 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0762× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 3.55 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0510× (z -9.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0589× (z -8.6) |
| [[A-427 (line)]] | wt | 6.40 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0526× (z -10.4) |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0933× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.08 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0883× (z -8.8) |
| [[A-172 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.527 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC63]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SNCA]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ZFHX4]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SFMBT2]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[FAT4]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 | STRING 427 |
| [[KCNH5]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | pathway: Neuronal System |
| [[FGF14]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ASXL3]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PDE1A]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CDH10]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL3]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02945]] | B | LINC02945 activity raises SLITRK5's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 1.72× lower at baseline in the lines without LINC02945 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016 |
| [[CDH10]] | C | CDH10 activity raises SLITRK5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.29× lower at baseline in the lines without CDH10 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises SLITRK5's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.04× lower at baseline in the lines without EPHA5 | 0.086 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises SLITRK5's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without ASXL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[HI-TOPK-032 (drug)]] 0.05 µM | C | SLITRK5 activity lowers the cells' numbers under HI-TOPK-032 0.05 µM (makes them more sensitive) | lines that do not express SLITRK5 (23) vs lines expressing it (25) | the lines without SLITRK5: 1.28× the cells of the other lines | 0.073 | ⚠ tissue-confounded; across organs; also absent: UCHL1, ZFHX4, VAT1L |
| cells under [[Ixazomib (drug)]] 0.05 µM | C | SLITRK5 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express SLITRK5 (23) vs lines expressing it (25) | the lines without SLITRK5: 1.21× the cells of the other lines | 0.085 | ⚠ tissue-confounded; across organs; also absent: UCHL1, ZFHX4, VAT1L |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | SLITRK5 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SLITRK5 (23) vs lines expressing it (25) | the lines without SLITRK5: 1.21× the cells of the other lines | 0.099 | ⚠ tissue-confounded; across organs; also absent: UCHL1, ZFHX4, VAT1L |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 35.2); signed map (39.5, 38.1). **Vector** length 58.5, 14.8% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +5.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.7 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SLIT and NTRK like family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.2 — chr13:87,671,371-87,696,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA364G4.2, KIAA0918; previously LRRC11 |
| Gene groups (HGNC) | SLIT and NTRK like family |
| Reactome | 8 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; RAC2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O94991](https://www.uniprot.org/uniprotkb/O94991) (SLIT and NTRK-like protein 5):

> Suppresses neurite outgrowth.

**Summary**, from NCBI Gene [26050](https://www.ncbi.nlm.nih.gov/gene/26050):

> Members of the SLITRK family, such as SLITRK5, are integral membrane proteins with 2 N-terminal leucine-rich repeat (LRR) domains similar to those of SLIT proteins (see SLIT1; MIM 603742). Most SLITRKs, including SLITRK5, also have C-terminal regions that share homology with neurotrophin receptors (see NTRK1; MIM 191315). SLITRKs are expressed predominantly in neural tissues and have neurite-modulating activity (Aruga et al., 2003 [PubMed 14557068]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20295) · Entrez [26050](https://www.ncbi.nlm.nih.gov/gene/26050) · UniProt [O94991](https://www.uniprot.org/uniprotkb/O94991) · Ensembl [ENSG00000165300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165300)

## Data

Gene col 9104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9104); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9104]; `tensor/DDL_lfc|DDL_z.npy` [9104]; `embed/gene_vectors.npy` [9104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9104 or target_col == 9104). Every well: [[SLITRK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLITRK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
