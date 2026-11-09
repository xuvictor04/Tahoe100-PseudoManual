---
symbol: "PDE4B"
type: "gene"
col: 11555
ensembl_id: "ENSG00000184588"
name: "phosphodiesterase 4B"
location: "1p31.3"
module: 19
arm: "+"
pooled_cpm: 92.65
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 12
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE4B

*phosphodiesterase 4B* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +9.8, q 5e-20, up in 5 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.503× (z -10.3, q 4e-22, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE7B]] (+0.72, fdr 7e-06), [[TCF4]] (+0.67, fdr 7e-06), [[PDE3A]] (+0.63, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[EDARADD]] → it (grade B ⚠); 3 go from it, the strongest it → [[PDE4D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.8 | 5e-20 | 5/25 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.22×** | +9.2 | 1e-17 | 19/25 (SW48, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +6.5 | 1e-08 | 14/24 (SW48, SW1417, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.5 | 5e-06 | 2/25 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 2e-04 | 2/24 (NCI-H1792, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.002 | 6/24 (HOP62, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.002 | 5/24 (LOX-IMVI, SW48, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.003 | 5/24 (A-427, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.005 | 6/24 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.024 | 12/24 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.4 | 0.039 | 0/22 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.057 | 2/25 (HOP62, SNU-423) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.073 | 6/24 (A549, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.083 | 4/25 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.090 | 9/24 (NCI-H460, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.503×** | -10.3 | 4e-22 | 21/24 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -9.1 | 4e-17 | 19/24 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -8.5 | 5e-15 | 22/24 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -5.4 | 9e-06 | 12/24 (SHP-77, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -5.2 | 3e-05 | 14/24 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -4.5 | 6e-04 | 17/24 (SW48, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 0.003 | 5/24 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.8 | 0.011 | 15/25 (NCI-H23, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.7 | 0.011 | 10/24 (SW48, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.7 | 0.011 | 16/24 (NCI-H23, H4, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.6 | 0.014 | 1/26 (NCI-H1792) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.6 | 0.014 | 16/24 (AN3 CA, NCI-H460, …) | two highest doses | composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.014 | 12/25 (A549, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.788×** | -3.5 | 0.016 | 12/24 (H4, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.793×** | -3.4 | 0.022 | 16/24 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.025 | 13/24 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.027 | 1/23 (LOX-IMVI) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.800×** | -3.3 | 0.027 | 7/23 (SNU-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.034 | 17/24 (SW48, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 170 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0924× (z -15.4) |
| [[SHP-77 (line)]] | alt | 772 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -16.5) |
| [[SW48 (line)]] | wt | 752 | 2 | 11 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 27.5× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -24.3) |
| [[NCI-H460 (line)]] | wt | 246 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -23.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -14.0) |
| [[SNU-1 (line)]] | wt | 2,128 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0236× (z -30.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -19.3) |
| [[A-427 (line)]] | wt | 321 | 1 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.0814× (z -23.3) |
| [[AN3 CA (line)]] | alt | 516 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -25.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -18.1) |
| [[A549 (line)]] | wt | 242 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.8) |
| [[H4 (line)]] | wt | 68.8 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0497× (z -15.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.127× (z -11.0) |
| [[SW1417 (line)]] | alt | 74.8 | 1 | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.7× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 67.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -8.9) |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.154× (z -8.5) |
| [[CHP-212 (line)]] | wt | 92.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 34.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 20.6× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 236 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -10.9) |
| [[LoVo (line)]] | wt | 31.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 23.6× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -9.1) |
| [[A-172 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.33 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7B]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | same gene group |
| [[TCF4]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PDE3A]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[FGF14]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[PDE10A]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 | same gene group |
| [[CDH7]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ADARB2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CDH10]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[COL4A5]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KCNH5]] | +0.59 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDARADD]] | B | EDARADD activity raises PDE4B's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without EDARADD | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3 |
| [[COL5A2]] | B | COL5A2 activity raises PDE4B's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without COL5A2 | 0.078 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[UNC5D]] | C | UNC5D activity raises PDE4B's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 4.57× lower at baseline in the lines without UNC5D | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises PDE4B's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 7.10× lower at baseline in the lines without KCNB2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises PDE4B's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without EPHA5-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises PDE4B's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.82× lower at baseline in the lines without TCF4 | 0.039 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises PDE4B's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.80× lower at baseline in the lines without PDE3A | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[PDE7B]] | C | PDE7B activity raises PDE4B's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without PDE7B | 0.053 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | HGF activity raises PDE4B's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.24× lower at baseline in the lines without HGF | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises PDE4B's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without EPHA5 | 0.062 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises PDE4B's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.43× lower at baseline in the lines without NCKAP5-AS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises PDE4B's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without CTNNA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4D]] | B | PDE4B activity raises PDE4D's level | lines that do not express PDE4B (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without PDE4B | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCSK2, MAPK4, UNC5D |
| [[COL4A5]] | C | PDE4B activity raises COL4A5's level | lines that do not express PDE4B (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without PDE4B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCSK2, MAPK4, UNC5D; co-absent with the target |
| [[TCF4]] | C | PDE4B activity raises TCF4's level | lines that do not express PDE4B (24) vs lines expressing it (26) | 4.72× lower at baseline in the lines without PDE4B | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCSK2, MAPK4, UNC5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.5, 34.0); signed map (37.8, 43.0). **Vector** length 93.0, 27.2% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | -0.3 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.0 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.9 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:65,792,514-66,374,579 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DPDE4 |
| Gene groups (HGNC) | Phosphodiesterases |
| Hallmark sets | INFLAMMATORY_RESPONSE, DNA_REPAIR, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: DARPP-32 events; Opioid Signalling; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07343](https://www.uniprot.org/uniprotkb/Q07343) (3',5'-cyclic-AMP phosphodiesterase 4B):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes. May be involved in mediating central nervous system effects of therapeutic agents ranging from antidepressants to antiasthmatic and anti-inflammatory agents.

**Summary**, from NCBI Gene [5142](https://www.ncbi.nlm.nih.gov/gene/5142):

> This gene is a member of the type IV, cyclic AMP (cAMP)-specific, cyclic nucleotide phosphodiesterase (PDE) family. The encoded protein regulates the cellular concentrations of cyclic nucleotides and thereby play a role in signal transduction. Altered activity of this protein has been associated with schizophrenia and bipolar affective disorder. Alternative splicing and the use of alternative promoters results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul …

**Accessions** — [HGNC:8781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8781) · Entrez [5142](https://www.ncbi.nlm.nih.gov/gene/5142) · UniProt [Q07343](https://www.uniprot.org/uniprotkb/Q07343) · Ensembl [ENSG00000184588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184588)

## Data

Gene col 11555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11555); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11555]; `tensor/DDL_lfc|DDL_z.npy` [11555]; `embed/gene_vectors.npy` [11555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11555 or target_col == 11555). Every well: [[PDE4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
