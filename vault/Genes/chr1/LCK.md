---
symbol: "LCK"
type: "gene"
col: 11335
ensembl_id: "ENSG00000182866"
name: "LCK proto-oncogene, Src family tyrosine kinase"
location: "1p35.2"
module: 31
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 19
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 27
direction_downstream: 40
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LCK

*LCK proto-oncogene, Src family tyrosine kinase* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.09× (z +14.9, q 0e+00, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.65× (z +9.7, q 7e-20, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.521× (z -4.5, q 0.003, down in 6 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PADI1]] (+0.81, fdr 7e-06), [[BLACAT1]] (+0.75, fdr 7e-06), [[LEMD1]] (+0.74, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 40 go from it, the strongest it → [[EPHB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.09×** | +14.9 | 0e+00 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.81×** | +12.4 | 1e-32 | 2/5 (NCI-H2347, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +9.7 | 7e-20 | 2/12 (HOP62, NCI-H2030) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.30×** | +9.5 | 4e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +9.3 | 1e-18 | 3/12 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.09×** | +7.9 | 2e-13 | 3/11 (HOP62, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.2 | 2e-05 | 1/5 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.64×** | +4.7 | 1e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.5 | 4e-04 | 1/7 (CFPAC-1) | top dose only | cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +4.0 | 0.004 | 1/5 (CFPAC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +3.9 | 0.006 | 1/4 (CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.7 | 0.009 | 1/11 (SW1417) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.011 | 7/14 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.68×** | +3.6 | 0.011 | 1/9 (HepG2/C3A) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +3.6 | 0.014 | 5/13 (KATO III, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.026 | 3/14 (SW480, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.82×** | +3.0 | 0.074 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.81×** | +3.0 | 0.078 | 3/14 (SW1417, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.52×** | +2.9 | 0.078 | 0/11 | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +2.9 | 0.084 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +2.9 | 0.088 | 5/13 (SW1417, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.521×** | -4.5 | 0.003 | 6/14 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.660×** | -4.1 | 0.012 | 6/14 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.686×** | -3.7 | 0.039 | 8/14 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.599×** | -3.6 | 0.039 | 8/12 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -3.5 | 0.049 | 1/14 (SW1417) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 5 µM |  | **0.405×** | -3.3 | 0.077 | 3/14 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.605×** | -3.3 | 0.078 | 6/14 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.653× | -3.0 | 0.17 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.5) |
| [[COLO 205 (line)]] | alt | 43.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.3) |
| [[LoVo (line)]] | wt | 3.46 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0477× (z -10.2) |
| [[A-172 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.596 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PADI1]] | +0.81 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[BLACAT1]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LEMD1]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PIWIL1]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 | pathway: Co-inhibition by PD-1 |
| [[INPP5D]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 521 |
| [[FGF19]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | pathway: Constitutive Signaling by Aberrant PI3K in Cancer |
| [[ONECUT3]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[ANO1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TLDC2]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 4, C 23. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises LCK's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BLACAT1]] | B | BLACAT1 activity raises LCK's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without BLACAT1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[MAP2K2]] | B | MAP2K2 activity raises LCK's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[IL19]] | B | IL19 activity raises LCK's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without IL19 | 0.078 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[CEACAM1]] | C | CEACAM1 activity raises LCK's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.10× lower at baseline in the lines without CEACAM1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises LCK's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.92× lower at baseline in the lines without GJB1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises LCK's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.66× lower at baseline in the lines without TFF3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises LCK's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without EPS8L3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[FGD5]] | C | FGD5 activity raises LCK's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.23× lower at baseline in the lines without FGD5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises LCK's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.34× lower at baseline in the lines without HNF4A | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises LCK's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without PIWIL1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[PIK3AP1]] | C | PIK3AP1 activity raises LCK's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without PIK3AP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 13, C 27. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | LCK activity raises EPHB3's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without LCK | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[LYPD3]] | B | LCK activity raises LYPD3's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without LCK | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[TMC6]] | B | LCK activity raises TMC6's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.81× lower at baseline in the lines without LCK | 0.023 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[DEF6]] | B | LCK activity raises DEF6's level | lines that do not express LCK (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without LCK | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[STON2]] | B | LCK activity raises STON2's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without LCK | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[VILL]] | B | LCK activity strengthens VILL's drug response | lines that do not express LCK (18) vs lines expressing it (12) | the lines without LCK respond 0.42× as strongly (z diff +1.88); strongest at Idarubicin (hydrochloride) 0.5 µM: 0.69x vs 0.27x (z diff +3.6) | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DEF6]] | B | LCK activity strengthens DEF6's drug response | lines that do not express LCK (25) vs lines expressing it (16) | the lines without LCK respond 0.68× as strongly (z diff +1.31); strongest at Homoharringtonine 5 µM: 0.60x vs 0.51x (z diff +2.5) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BLACAT1]] | B | LCK activity raises BLACAT1's level | lines that do not express LCK (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without LCK | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[LEMD1]] | B | LCK activity raises LEMD1's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without LCK | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[CEMIP]] | B | LCK activity raises CEMIP's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without LCK | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[FBLIM1]] | B | LCK activity strengthens FBLIM1's drug response | lines that do not express LCK (22) vs lines expressing it (16) | the lines without LCK respond 0.76× as strongly (z diff +1.79); strongest at Homoharringtonine 5 µM: 0.51x vs 0.31x (z diff +4.1) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FBLIM1]] | B | LCK activity raises FBLIM1's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LCK | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 52.3); signed map (3.5, 38.8). **Vector** length 43.1, 12.6% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | LCK proto-oncogene, Src family tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,251,244-32,286,165 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Hallmark sets | BILE_ACID_METABOLISM, PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, COMPLEMENT |
| Reactome | 52 pathways, smallest: FLT3 signaling through SRC family kinases; Translocation of ZAP-70 to Immunological synapse; Nef and signal transduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P06239](https://www.uniprot.org/uniprotkb/P06239) (Tyrosine-protein kinase Lck):

> Non-receptor tyrosine-protein kinase that plays an essential role in the selection and maturation of developing T-cells in the thymus and in the function of mature T-cells. Plays a key role in T-cell antigen receptor (TCR)-linked signal transduction pathways. Constitutively associated with the cytoplasmic portions of the CD4 and CD8 surface receptors. Association of the TCR with a peptide antigen-bound MHC complex facilitates the interaction of CD4 and CD8 with MHC class II and class I …

**Summary**, from NCBI Gene [3932](https://www.ncbi.nlm.nih.gov/gene/3932):

> This gene is a member of the Src family of protein tyrosine kinases (PTKs). The encoded protein is a key signaling molecule in the selection and maturation of developing T-cells. It contains N-terminal sites for myristylation and palmitylation, a PTK domain, and SH2 and SH3 domains which are involved in mediating protein-protein interactions with phosphotyrosine-containing and proline-rich motifs, respectively. The protein localizes to the plasma membrane and pericentrosomal vesicles, and binds …

**Accessions** — [HGNC:6524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6524) · Entrez [3932](https://www.ncbi.nlm.nih.gov/gene/3932) · UniProt [P06239](https://www.uniprot.org/uniprotkb/P06239) · Ensembl [ENSG00000182866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182866)

## Data

Gene col 11335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11335); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11335]; `tensor/DDL_lfc|DDL_z.npy` [11335]; `embed/gene_vectors.npy` [11335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11335 or target_col == 11335). Every well: [[LCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
