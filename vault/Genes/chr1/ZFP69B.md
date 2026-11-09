---
symbol: "ZFP69B"
type: "gene"
col: 11952
ensembl_id: "ENSG00000187801"
name: "ZFP69 zinc finger protein B"
location: "1p34.2"
module: 1
arm: "+"
pooled_cpm: 5.56
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZFP69B

*ZFP69 zinc finger protein B* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.98× (z +8.2, q 1e-13, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.439× (z -9.9, q 2e-20, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETV3]] (+0.55, fdr 2e-05), [[MAK16]] (+0.55, fdr 3e-05), [[ZFP69]] (+0.55, fdr 1e-05, ⚠ same locus), [[TOMM34]] (+0.55, fdr 4e-05); moves opposite to [[NPC2]] (-0.56, fdr 2e-05), [[ATOSA]] (-0.53, fdr 1e-05), [[MICU1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PARVG]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +8.2 | 1e-13 | 23/38 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.9 | 1e-06 | 12/40 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.66×** | +5.8 | 1e-06 | 13/25 (A-427, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.62×** | +5.8 | 1e-06 | 12/41 (LoVo, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.65×** | +5.7 | 1e-06 | 2/7 (HS-578T, HOP62) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +4.6 | 3e-04 | 8/41 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +4.6 | 4e-04 | 7/40 (HOP62, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.43×** | +4.3 | 0.001 | 13/41 (SNU-423, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.2 | 0.002 | 7/41 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.003 | 7/41 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.9 | 0.004 | 6/42 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.034 | 7/41 (NCI-H2030, C-33 A, …) | rises with dose | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.034 | 3/37 (PANC-1, C-33 A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +3.1 | 0.074 | 8/38 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.1 | 0.074 | 2/21 (NCI-H2030, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.439×** | -9.9 | 2e-20 | 25/38 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.466×** | -9.2 | 1e-17 | 29/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -5.9 | 8e-07 | 19/33 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -5.5 | 5e-06 | 18/39 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -4.2 | 0.003 | 15/41 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.721×** | -3.8 | 0.014 | 7/41 (CHP-212, COLO 205, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.649×** | -3.7 | 0.016 | 10/30 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.11 | 6/37 (RPMI-7951, SHP-77, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.11 | 10/32 (SW480, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.10 | 0 | 5 (3 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.110× (z -10.6) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 9.67 | 0 | 2 | — | [[Omeprazole (drug)]] 0.5 µM 0.120× (z -10.6) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.331× (z -8.9) |
| [[A-427 (line)]] | wt | 9.57 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 3.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 4.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0443× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0854× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.06 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[SW480 (line)]] | alt | 3.37 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0981× (z -10.3) |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.993 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETV3]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[MAK16]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ZFP69]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 | same gene group; ⚠ same locus (13.6 kb, same strand: neighbours can correlate without regulation) |
| [[TOMM34]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[VEPH1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 | same gene group |
| [[TXLNA]] | +0.51 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[EIF3D]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CCT5]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PABPC1L]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[RGS4]] | +0.50 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[RBAK]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 | same gene group |
| [[RDUR]] | +0.48 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC2]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ATOSA]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MICU1]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC16]] | -0.51 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[AAMDC]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ELF2]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ZFYVE1]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HECTD4]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[GABARAP]] ⚠ | -0.50 | -0.46 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TOM1L2]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TOM1]] | -0.47 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[SPPL3]] | -0.47 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[GAB1]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVG]] | B | PARVG activity raises ZFP69B's level | lines that do not express PARVG (15) vs lines expressing it (35) | 2.23× lower at baseline in the lines without PARVG | 0.035 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSR1]] | B | ZFP69B activity raises TSR1's level | lines that do not express ZFP69B (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without ZFP69B | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: LINC00888, PDE4C, RIMS3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (51.7, -7.5); signed map (13.1, 57.4). **Vector** length 56.4, 7.91% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -9.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -9.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.5 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ZFP69 zinc finger protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,450,102-40,463,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZKSCAN23B, FLJ34293, ZSCAN54B; previously ZNF643 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJL9](https://www.uniprot.org/uniprotkb/Q9UJL9) (Zinc finger protein 69 homolog B):

> May be involved in transcriptional regulation. Essential for Golgi structural integrity.

**Summary**, from NCBI Gene [65243](https://www.ncbi.nlm.nih.gov/gene/65243):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in Golgi organization. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28053) · Entrez [65243](https://www.ncbi.nlm.nih.gov/gene/65243) · UniProt [Q9UJL9](https://www.uniprot.org/uniprotkb/Q9UJL9) · Ensembl [ENSG00000187801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187801)

## Data

Gene col 11952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11952); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11952]; `tensor/DDL_lfc|DDL_z.npy` [11952]; `embed/gene_vectors.npy` [11952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11952 or target_col == 11952). Every well: [[ZFP69B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP69B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
