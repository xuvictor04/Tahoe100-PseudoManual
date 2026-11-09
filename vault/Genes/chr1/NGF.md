---
symbol: "NGF"
type: "gene"
col: 5532
ensembl_id: "ENSG00000134259"
name: "nerve growth factor"
location: "1p13.2"
module: 125
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 19
n_dd_up: 43
n_dd_down: 6
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# NGF

*nerve growth factor* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.15× (z +16.0, q 0e+00, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.628× (z -4.7, q 0.002, down in 6 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02154]] (+0.73, fdr 7e-06), [[SLAMF7]] (+0.69, fdr 7e-06), [[ROR1-AS1]] (+0.67, fdr 7e-06).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BMPER]] → it (grade B ⚠); 9 go from it, the strongest it → [[CRYM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.15×** | +16.0 | 0e+00 | 13/17 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +11.6 | 7e-29 | 14/17 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.9 | 3e-25 | 1/13 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +10.6 | 7e-24 | 0/7 | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +10.1 | 8e-22 | 14/17 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +9.8 | 1e-20 | 0/7 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.22×** | +7.8 | 4e-13 | 14/17 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +7.6 | 2e-12 | 11/17 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.1 | 1e-10 | 11/16 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.9 | 2e-07 | 4/14 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +4.9 | 5e-05 | 12/16 (J82, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.9 | 5e-05 | 5/13 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 8e-05 | 2/16 (NCI-H1573, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 2e-04 | 10/17 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.90×** | +4.5 | 2e-04 | 5/17 (NCI-H460, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +4.4 | 3e-04 | 10/17 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 4e-04 | 5/17 (NCI-H1573, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 8e-04 | 8/17 (BT-474, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.001 | 4/17 (BT-474, A-172, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.002 | 10/16 (NCI-H460, SK-MEL-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.007 | 4/17 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.628×** | -4.7 | 0.002 | 6/17 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.762×** | -3.9 | 0.028 | 7/17 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.691×** | -3.7 | 0.037 | 7/17 (HS-578T, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.6 | 0.038 | 3/17 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.667×** | -3.6 | 0.038 | 2/17 (NCI-H460, BT-474) | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | **0.525×** | -3.3 | 0.094 | 0/17 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.725×** | -3.2 | 0.096 | 5/17 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.701× | -3.1 | 0.12 | 1/17 (BT-474) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.811× | -3.0 | 0.16 | 0/17 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 128 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -24.0) |
| [[J82 (line)]] | alt | 68.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.2) |
| [[HS-578T (line)]] | alt | 55.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +17.2) | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 4.31 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.84× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.753 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.596 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02154]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SLAMF7]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[HDAC9]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ADAMTS16]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ENTHD1]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MIR155HG]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CREB5]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FAM110B]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MSR1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC01435]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PSG4]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | BMPER activity raises NGF's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.82× lower at baseline in the lines without BMPER | 0.059 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[EML5]] | B | EML5 activity raises NGF's level | lines that do not express EML5 (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without EML5 | 0.069 | ⚠ within organs, on part of the lines; also absent: HOXA7, DOCK3, ENPP4; maybe low, not absent |
| [[LINC01060]] | C | LINC01060 activity raises NGF's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without LINC01060 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM; co-absent with the target |
| [[LINC00536]] | C | LINC00536 activity raises NGF's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 3.32× lower at baseline in the lines without LINC00536 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises NGF's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 4.49× lower at baseline in the lines without IRAG2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises NGF's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without SHISAL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[LINC01828]] | C | LINC01828 activity raises NGF's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 3.00× lower at baseline in the lines without LINC01828 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYM]] | B | NGF activity raises CRYM's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without NGF | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[C12orf50]] | B | NGF activity raises C12orf50's level | lines that do not express NGF (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without NGF | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[DUSP10]] | B | NGF activity raises DUSP10's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.43× lower at baseline in the lines without NGF | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[CYRIA]] | B | NGF activity raises CYRIA's level | lines that do not express NGF (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without NGF | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1 |
| [[LINC01060]] | C | NGF activity raises LINC01060's level | lines that do not express NGF (31) vs lines expressing it (19) | 3.54× lower at baseline in the lines without NGF | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[ABI3BP]] | C | NGF activity raises ABI3BP's level | lines that do not express NGF (31) vs lines expressing it (19) | 4.02× lower at baseline in the lines without NGF | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[SLAMF7]] | C | NGF activity raises SLAMF7's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without NGF | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[NAALADL2-AS2]] | C | NGF activity raises NAALADL2-AS2's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without NGF | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[LINC02968]] | C | NGF activity raises LINC02968's level | lines that do not express NGF (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without NGF | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, 21.8); signed map (38.4, 23.0). **Vector** length 54.0, 14.3% of its response variance represented; |z| ≥ 3 in 492 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nerve growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:115,285,904-115,338,770 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NGFB |
| Gene groups (HGNC) | Neurotrophins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, KRAS_SIGNALING_UP |
| Reactome | 30 pathways, smallest: Ceramide signalling; NFG and proNGF binds to p75NTR; PLC-gamma1 signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P01138](https://www.uniprot.org/uniprotkb/P01138) (Beta-nerve growth factor):

> Nerve growth factor is important for the development and maintenance of the sympathetic and sensory nervous systems. Extracellular ligand for the NTRK1 and NGFR receptors, activates cellular signaling cascades to regulate neuronal proliferation, differentiation and survival (Probable). The immature NGF precursor (proNGF) functions as a ligand for the heterodimeric receptor formed by SORCS2 and NGFR, and activates cellular signaling cascades that lead to inactivation of RAC1 and/or RAC2, …

**Summary**, from NCBI Gene [4803](https://www.ncbi.nlm.nih.gov/gene/4803):

> This gene is a member of the NGF-beta family and encodes a secreted protein which homodimerizes and is incorporated into a larger complex. This protein has nerve growth stimulating activity and the complex is involved in the regulation of growth and the differentiation of sympathetic and certain sensory neurons. Mutations in this gene have been associated with hereditary sensory and autonomic neuropathy, type 5 (HSAN5), and dysregulation of this gene's expression is associated with allergic …

**Accessions** — [HGNC:7808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7808) · Entrez [4803](https://www.ncbi.nlm.nih.gov/gene/4803) · UniProt [P01138](https://www.uniprot.org/uniprotkb/P01138) · Ensembl [ENSG00000134259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134259)

## Data

Gene col 5532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5532); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5532]; `tensor/DDL_lfc|DDL_z.npy` [5532]; `embed/gene_vectors.npy` [5532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5532 or target_col == 5532). Every well: [[NGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
