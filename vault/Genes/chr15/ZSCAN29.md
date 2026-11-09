---
symbol: "ZSCAN29"
type: "gene"
col: 6382
ensembl_id: "ENSG00000140265"
name: "zinc finger and SCAN domain containing 29"
location: "15q15.3"
module: 7
arm: "+"
pooled_cpm: 14.25
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZSCAN29

*zinc finger and SCAN domain containing 29* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.76× (z +6.7, q 1e-08, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.552× (z -7.1, q 7e-10, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF629]] (+0.80, fdr 7e-06), [[ZNF747]] (+0.76, fdr 1e-05), [[CBLL1]] (+0.75, fdr 7e-06); moves opposite to [[GMCL1]] (-0.75, fdr 7e-06), [[PPP1R2]] (-0.69, fdr 1e-05), [[EFHC1]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MARVELD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.7 | 1e-08 | 29/46 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.4 | 4e-08 | 28/44 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.0 | 3e-07 | 31/47 (LoVo, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.3 | 2e-05 | 22/48 (hTERT-HPNE, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +4.9 | 9e-05 | 24/44 (SW480, HCT15, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.6 | 4e-04 | 21/40 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 4e-04 | 12/21 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +4.5 | 4e-04 | 21/46 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 19/48 (A498, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 18/47 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 20/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.5 | 0.019 | 8/29 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.027 | 17/47 (LoVo, Panc 03.27, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.040 | 8/47 (CFPAC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.044 | 16/47 (AsPC-1, HOP62, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.067 | 13/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.067 | 11/44 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.067 | 14/44 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -7.1 | 7e-10 | 31/47 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -6.4 | 4e-08 | 28/46 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -6.4 | 4e-08 | 28/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -5.5 | 5e-06 | 28/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -4.4 | 0.001 | 22/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -3.9 | 0.010 | 19/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0594× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Proglumide (drug)]] 0.05 µM 0.0748× (z -10.2) |
| [[A-172 (line)]] | wt | 5.69 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0833× (z -9.7) |
| [[A549 (line)]] | wt | 10.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0938× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.338× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 | — | [[AZD-7648 (drug)]] 5 µM 0.0750× (z -8.6) |
| [[A-427 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF629]] | +0.80 | +0.79 / +0.72 | both halves | 7e-06 | same gene group |
| [[ZNF747]] | +0.76 | +0.74 / +0.57 | both halves | 1e-05 | same gene group |
| [[CBLL1]] | +0.75 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ZNF594]] | +0.74 | +0.73 / +0.64 | both halves | 7e-06 | same gene group |
| [[TACO1]] | +0.73 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[BCDIN3D]] | +0.73 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[ZXDB]] | +0.73 | +0.70 / +0.57 | both halves | 8e-06 | same gene group |
| [[HCCS]] | +0.73 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.72 | +0.77 / +0.40 | both halves | 4e-05 | same gene group |
| [[MOCS3]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.75 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[PPP1R2]] | -0.69 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[EFHC1]] | -0.69 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.67 | -0.73 / -0.41 | both halves | 4e-05 |  |
| [[HSPB11]] | -0.67 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[RFX2]] | -0.64 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.64 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ARL3]] | -0.64 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARVELD2]] | B | MARVELD2 activity raises ZSCAN29's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without MARVELD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ZSCAN29's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises ZSCAN29's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.06× lower at baseline in the lines without ALOX12P2-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.3, 8.3); signed map (13.0, -22.0). **Vector** length 90.1, 18.6% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.8 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,358,172-43,371,043 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35867, Zfp690; previously ZNF690 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWY8](https://www.uniprot.org/uniprotkb/Q8IWY8) (Zinc finger and SCAN domain-containing protein 29):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [146050](https://www.ncbi.nlm.nih.gov/gene/146050):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26673) · Entrez [146050](https://www.ncbi.nlm.nih.gov/gene/146050) · UniProt [Q8IWY8](https://www.uniprot.org/uniprotkb/Q8IWY8) · Ensembl [ENSG00000140265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140265)

## Data

Gene col 6382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6382); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6382]; `tensor/DDL_lfc|DDL_z.npy` [6382]; `embed/gene_vectors.npy` [6382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6382 or target_col == 6382). Every well: [[ZSCAN29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
