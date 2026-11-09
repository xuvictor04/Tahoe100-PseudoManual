---
symbol: "MAPK12"
type: "gene"
col: 11978
ensembl_id: "ENSG00000188130"
name: "mitogen-activated protein kinase 12"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAPK12

*mitogen-activated protein kinase 12* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +7.9, q 2e-12, up in 11 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.67× (z +4.3, q 0.002, up in 8 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -13.6, q 3e-39, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGHG]] (+0.71, fdr 7e-06), [[NECAB3]] (+0.68, fdr 8e-06), [[KLHL17]] (+0.67, fdr 7e-06); moves opposite to [[SNRPB2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.9 | 2e-12 | 11/13 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.5 | 2e-11 | 17/30 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +5.4 | 1e-05 | 8/19 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.1 | 6e-05 | 16/34 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 0.002 | 8/33 (SW48, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.007 | 12/37 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.8 | 0.010 | 6/19 (PANC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.050 | 10/39 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -13.6 | 3e-39 | 34/43 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -10.0 | 3e-21 | 28/43 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -8.9 | 1e-16 | 30/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.495×** | -8.4 | 8e-15 | 31/46 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -7.7 | 2e-12 | 33/45 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.531×** | -7.5 | 4e-12 | 28/46 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -5.7 | 1e-06 | 22/41 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.437×** | -5.2 | 2e-05 | 19/43 (LOX-IMVI, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -4.9 | 6e-05 | 17/43 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -4.6 | 3e-04 | 17/45 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -4.4 | 5e-04 | 17/47 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.701×** | -4.2 | 0.001 | 14/41 (HOP62, NCI-H1573, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.054 | 8/46 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.608×** | -3.1 | 0.076 | 5/38 (Hs 766T, C-33 A, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.765×** | -3.0 | 0.099 | 13/41 (A-427, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.1) |
| [[PANC-1 (line)]] | alt | 9.68 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -13.3) |
| [[SW48 (line)]] | wt | 10.9 | 0 | 2 | — | [[Vandetanib (drug)]] 0.05 µM 0.0743× (z -9.4) |
| [[A-427 (line)]] | wt | 8.97 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0909× (z -11.5) |
| [[A498 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.8) |
| [[A549 (line)]] | wt | 5.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -14.1) |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0536× (z -8.7) |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0939× (z -10.2) |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0703× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 8.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 5.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -8.9) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.7) |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[SW480 (line)]] | alt | 7.64 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -8.6) |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGHG]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NECAB3]] | +0.68 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[KLHL17]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[KAT2A]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[NBEAL2]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MED16]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[B4GALNT4]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SLC19A1]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MAPK11]] | +0.64 | +0.72 / +0.57 | both halves | 1e-05 | same gene group; pathway: Activation of PPARGC1A (PGC-1alpha) by phosphorylation; STRING 856; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[AKT1]] | +0.63 | +0.68 / +0.59 | both halves | 7e-06 | pathway: Signaling by VEGF; STRING 937 |
| [[HDAC10]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NSMF]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[EML3]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises MAPK12's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without ADCY3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[GNAZ]] | B | GNAZ activity raises MAPK12's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without GNAZ | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[NCS1]] | B | NCS1 activity raises MAPK12's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without NCS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[SEPTIN5]] | B | SEPTIN5 activity raises MAPK12's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without SEPTIN5 | 0.024 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[BRSK2]] | B | BRSK2 activity raises MAPK12's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without BRSK2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[SLC4A3]] | B | SLC4A3 activity raises MAPK12's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without SLC4A3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[B4GALNT4]] | B | B4GALNT4 activity strengthens MAPK12's drug response | lines that do not express B4GALNT4 (17) vs lines expressing it (29) | the lines without B4GALNT4 respond 0.67× as strongly (z diff +1.25); strongest at Belinostat 5 µM: 0.66x vs 0.42x (z diff +2.2) | 0.068 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[BRSK2]] | B | BRSK2 activity strengthens MAPK12's drug response | lines that do not express BRSK2 (14) vs lines expressing it (32) | the lines without BRSK2 respond 0.58× as strongly (z diff +1.61); strongest at Belinostat 5 µM: 0.77x vs 0.41x (z diff +3.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises MAPK12's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.4, -24.4); signed map (-26.9, -0.5). **Vector** length 62.8, 9.48% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -10.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,245,450-50,261,716 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERK6, PRKM12, p38gamma, SAPK-3; previously SAPK3 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 11-14 (p38) family |
| Hallmark sets | MYOGENESIS |
| Reactome | 19 pathways, smallest: Activation of PPARGC1A (PGC-1alpha) by phosphorylation; p38MAPK events; Signalling to RAS |
| Matched by | ensembl_id |

**Function**, from UniProt [P53778](https://www.uniprot.org/uniprotkb/P53778) (Mitogen-activated protein kinase 12):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK12 is one of the four p38 MAPKs which play an important role in the cascades of cellular responses evoked by extracellular stimuli such as pro-inflammatory cytokines or physical stress leading to direct activation of transcription factors such as ELK1 and ATF2. Accordingly, p38 MAPKs phosphorylate a broad range of proteins and it has been estimated that they may have approximately 200 …

**Summary**, from NCBI Gene [6300](https://www.ncbi.nlm.nih.gov/gene/6300):

> Activation of members of the mitogen-activated protein kinase family is a major mechanism for transduction of extracellular signals. Stress-activated protein kinases are one subclass of MAP kinases. The protein encoded by this gene functions as a signal transducer during differentiation of myoblasts to myotubes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6874) · Entrez [6300](https://www.ncbi.nlm.nih.gov/gene/6300) · UniProt [P53778](https://www.uniprot.org/uniprotkb/P53778) · Ensembl [ENSG00000188130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188130)

## Data

Gene col 11978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11978); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11978]; `tensor/DDL_lfc|DDL_z.npy` [11978]; `embed/gene_vectors.npy` [11978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11978 or target_col == 11978). Every well: [[MAPK12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
