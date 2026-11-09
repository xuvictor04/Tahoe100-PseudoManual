---
symbol: "IDNK"
type: "gene"
col: 7239
ensembl_id: "ENSG00000148057"
name: "IDNK gluconokinase"
location: "9q21.32"
module: 10
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# IDNK

*IDNK gluconokinase* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +9.9, q 2e-20, up in 17 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +6.7, q 2e-09, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.354× (z -11.2, q 1e-26, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATE1OSP]] (+0.75, fdr 1e-05), [[PPP3CB-AS1]] (+0.75, fdr 7e-06), [[FAIM]] (+0.73, fdr 1e-05); moves opposite to [[FCHO1]] (-0.62, fdr 4e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STEAP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.9 | 2e-20 | 17/22 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +9.8 | 5e-20 | 12/16 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.6 | 1e-15 | 7/9 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.7 | 2e-09 | 24/40 (HCT15, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.6 | 6e-04 | 15/43 (A-427, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +4.5 | 7e-04 | 13/43 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.32×** | +4.2 | 0.002 | 10/46 (A498, LoVo, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.019 | 8/36 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.019 | 8/47 (LS 180, A498, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.028 | 7/41 (RKO, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.037 | 9/39 (J82, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.13 | 9/43 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.354×** | -11.2 | 1e-26 | 33/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -10.1 | 1e-21 | 35/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -8.8 | 3e-16 | 33/45 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.535×** | -6.8 | 2e-09 | 21/44 (BT-474, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -5.8 | 8e-07 | 22/47 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.590×** | -5.7 | 1e-06 | 22/41 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.623×** | -5.1 | 3e-05 | 21/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.721×** | -5.0 | 4e-05 | 17/40 (J82, PANC-1, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -4.7 | 2e-04 | 13/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.684×** | -4.1 | 0.002 | 12/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.689×** | -4.0 | 0.003 | 17/36 (PANC-1, J82, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.726×** | -3.5 | 0.025 | 14/43 (BT-474, LS 180, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.739×** | -3.3 | 0.048 | 11/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.723×** | -3.1 | 0.080 | 9/45 (A-427, J82, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.585×** | -3.0 | 0.090 | 8/43 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.41 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0528× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 6.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 9.57 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 4.06 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0597× (z -9.2) |
| [[SNU-423 (line)]] | alt | 4.19 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0559× (z -9.4) |
| [[SW480 (line)]] | alt | 4.91 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -8.6) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | +0.75 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.75 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[FAIM]] | +0.73 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.73 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[PJVK]] | +0.72 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.71 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TLK2]] | +0.71 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CDNF]] | +0.71 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[THBS4]] | +0.71 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[AHI1-DT]] | +0.71 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[PBLD]] | +0.70 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[HEXIM2-AS1]] | +0.70 | +0.59 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.62 | -0.50 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP2-AS1]] | B | STEAP2-AS1 activity lowers IDNK's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 1.36× higher at baseline in the lines without STEAP2-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[ZNF818P]] | B | ZNF818P activity lowers IDNK's level | lines that do not express ZNF818P (21) vs lines expressing it (29) | 1.33× higher at baseline in the lines without ZNF818P | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF347, ZNF93 |
| [[TOP2A]] | B | TOP2A activity lowers IDNK's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises IDNK's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without TMEM9B-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[SCART1]] | C | SCART1 activity lowers IDNK's level | lines that do not express SCART1 (3) vs lines expressing it (47) | 1.34× higher at baseline in the lines without SCART1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.6, 17.6); signed map (30.6, -13.4). **Vector** length 65.0, 10.3% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | IDNK gluconokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,623,049-83,644,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA522I20.2, hGntK; previously C9orf103 |
| Gene groups (HGNC) | Carbohydrate kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6J7](https://www.uniprot.org/uniprotkb/Q5T6J7) (Gluconokinase):

> [Isoform 1]: Phosphorylates gluconate to 6-phosphogluconate.

**Summary**, from NCBI Gene [414328](https://www.ncbi.nlm.nih.gov/gene/414328):

> Predicted to enable gluconokinase activity. Predicted to be involved in carbohydrate metabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31367) · Entrez [414328](https://www.ncbi.nlm.nih.gov/gene/414328) · UniProt [Q5T6J7](https://www.uniprot.org/uniprotkb/Q5T6J7) · Ensembl [ENSG00000148057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148057)

## Data

Gene col 7239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7239); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7239]; `tensor/DDL_lfc|DDL_z.npy` [7239]; `embed/gene_vectors.npy` [7239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7239 or target_col == 7239). Every well: [[IDNK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDNK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
