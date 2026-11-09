---
symbol: "PRDM11"
type: "gene"
col: 312
ensembl_id: "ENSG00000019485"
name: "PR/SET domain 11"
location: "11p11.2"
module: 137
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# PRDM11

*PR/SET domain 11* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +8.5, q 1e-14, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +7.5, q 2e-11, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.496× (z -9.0, q 2e-16, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLG5]] (+0.77, fdr 7e-06), [[FAIM]] (+0.74, fdr 1e-05), [[SLC25A21]] (+0.72, fdr 1e-04); moves opposite to [[PIBF1]] (-0.68, fdr 1e-05), [[EFNA4]] (-0.62, fdr 8e-05), [[GMCL1]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.5 | 1e-14 | 9/13 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.5 | 2e-11 | 21/43 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.3 | 5e-11 | 26/44 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.3 | 2e-05 | 15/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.44×** | +4.4 | 0.001 | 7/46 (SW480, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.9 | 0.010 | 10/28 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.028 | 13/47 (PANC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clofarabine (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.052 | 9/46 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.2 | 0.100 | 8/18 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 3/47 (J82, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.496×** | -9.0 | 2e-16 | 32/47 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.521×** | -8.3 | 2e-14 | 26/47 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -7.8 | 1e-12 | 24/46 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.546×** | -7.7 | 1e-12 | 26/47 (A549, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -4.0 | 0.008 | 20/42 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.743×** | -3.8 | 0.014 | 16/41 (A-172, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.030 | 11/46 (C32, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.622× | -3.2 | 0.11 | 9/45 (RKO, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 17.9 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.128× (z -9.5) |
| [[Hs 766T (line)]] | wt | 8.01 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.120× (z -8.6) |
| [[LoVo (line)]] | wt | 7.90 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.9× (z +14.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 6.30 | 0 | 2 (1 ⚠) | — | [[Isocorydine (drug)]] 0.5 µM 0.0694× (z -11.4) |
| [[A498 (line)]] | wt | 3.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +8.7) | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 6.70 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0871× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0938× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 6.16 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~67% of this change |
| [[LS 180 (line)]] | wt | 4.76 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0768× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 5.02 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -8.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[SW1417 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.36× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLG5]] | +0.77 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[FAIM]] | +0.74 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.72 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[ICA1L]] | +0.70 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[WNT3]] | +0.69 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[RCBTB2]] | +0.68 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ERMAP]] | +0.67 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[FKRP]] | +0.67 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[STRN4]] | +0.67 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PRRC2B]] | +0.67 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[POU6F1]] | +0.65 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[FIZ1]] | +0.64 | +0.55 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.68 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[EFNA4]] | -0.62 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GMCL1]] | -0.62 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[COX6A1]] | -0.60 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[EFHC1]] | -0.60 | -0.57 / -0.24 | both halves | 4e-04 |  |
| [[ANAPC11]] | -0.60 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[RASSF7]] | -0.59 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[CARHSP1]] | -0.59 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RAB20]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RALGAPA2]] | -0.58 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.58 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[PDCD10]] | -0.58 | -0.46 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PRDM11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAB20]] | B | RAB20 activity weakens PRDM11's drug response | lines that do not express RAB20 (8) vs lines expressing it (40) | the lines without RAB20 respond 1.20× as strongly (z diff -0.62); strongest at Belinostat 0.5 µM: 0.46x vs 0.67x (z diff -2.3) | 0.071 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SLC4A3]] | B | SLC4A3 activity raises PRDM11's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without SLC4A3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-6.1, 8.2); signed map (23.7, -27.3). **Vector** length 66.6, 9.69% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.0 | -9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -3.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,095,806-45,235,110 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFM8 |
| Gene groups (HGNC) | PR/SET domain family; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQV5](https://www.uniprot.org/uniprotkb/Q9NQV5) (PR domain-containing protein 11):

> May be involved in transcription regulation.

**Summary**, from NCBI Gene [56981](https://www.ncbi.nlm.nih.gov/gene/56981):

> Predicted to enable DNA-binding transcription factor activity; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and chromatin binding activity. Involved in several processes, including negative regulation of cell growth; positive regulation of fibroblast apoptotic process; and regulation of DNA-templated transcription. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13996) · Entrez [56981](https://www.ncbi.nlm.nih.gov/gene/56981) · UniProt [Q9NQV5](https://www.uniprot.org/uniprotkb/Q9NQV5) · Ensembl [ENSG00000019485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019485)

## Data

Gene col 312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 312); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 312]; `tensor/DDL_lfc|DDL_z.npy` [312]; `embed/gene_vectors.npy` [312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 312 or target_col == 312). Every well: [[PRDM11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
