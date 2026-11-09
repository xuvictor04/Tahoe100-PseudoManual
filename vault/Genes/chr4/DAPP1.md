---
symbol: "DAPP1"
type: "gene"
col: 942
ensembl_id: "ENSG00000070190"
name: "dual adaptor of phosphotyrosine and 3-phosphoinositides 1"
location: "4q23"
module: 8
arm: "+"
pooled_cpm: 20.79
n_lines_expressing: 11
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 84
direction_downstream: 114
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DAPP1

*dual adaptor of phosphotyrosine and 3-phosphoinositides 1* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +9.6, q 6e-19, up in 6 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.613× (z -4.6, q 0.003, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRF1]] (+0.70, fdr 7e-06), [[FAM83B]] (+0.69, fdr 7e-06), [[NECTIN4]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 114 go from it, the strongest it → [[LRATD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +9.6 | 6e-19 | 6/9 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +9.2 | 1e-17 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +9.0 | 3e-17 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +6.6 | 5e-09 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +6.0 | 2e-07 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +5.4 | 8e-06 | 8/9 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.9 | 7e-05 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.6 | 3e-04 | 0/9 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 4e-04 | 1/9 (BT-474) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.4 | 6e-04 | 2/9 (LS 180, AsPC-1) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 6e-04 | 4/9 (AsPC-1, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 8e-04 | 5/9 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.51×** | +3.8 | 0.006 | 7/9 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.006 | 0/9 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.012 | 5/9 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.014 | 7/10 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.015 | 4/9 (HT-29, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.028 | 6/9 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.028 | 4/9 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.033 | 2/9 (NCI-H2347, NCI-H1573) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.046 | 4/10 (HT-29, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.046 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -4.6 | 0.003 | 9/9 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -4.4 | 0.003 | 8/9 (BT-474, HT-29, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.666×** | -3.8 | 0.027 | 9/9 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.072 | 5/9 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.673× | -3.3 | 0.10 | 0/9 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.676× | -3.3 | 0.10 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 62.4 | 7 (4 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.0311× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 142 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0760× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 94.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -12.5) |
| [[HT-29 (line)]] | alt | 45.6 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -15.1) |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -13.3) |
| [[KATO III (line)]] | alt | 41.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 170 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -12.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.186× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.1) |
| [[A-172 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRF1]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[FAM83B]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NECTIN4]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MYO5B]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[HHLA2]] | +0.66 | +0.58 / +0.70 | both halves | 8e-06 | **novel candidate** |
| [[INAVA]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MACC1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[RNF39]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ADGRF4]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 10, C 74. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DAPP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EPS8L1]] | B | EPS8L1 activity raises DAPP1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without EPS8L1 | 0.053 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[LRATD2]] | B | LRATD2 activity raises DAPP1's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without LRATD2 | 0.055 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[EXPH5]] | B | EXPH5 activity raises DAPP1's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without EXPH5 | 0.058 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises DAPP1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without ELF3-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[IFNLR1]] | B | IFNLR1 activity raises DAPP1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.85× lower at baseline in the lines without IFNLR1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[PRRG4]] | B | PRRG4 activity raises DAPP1's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without PRRG4 | 0.081 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises DAPP1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without PLEKHG1 | 0.089 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LGALS9]] | B | LGALS9 activity raises DAPP1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.83× lower at baseline in the lines without LGALS9 | 0.094 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers DAPP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[TMPRSS2]] | C | TMPRSS2 activity raises DAPP1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 10.24× lower at baseline in the lines without TMPRSS2 | 6e-05 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises DAPP1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 8.17× lower at baseline in the lines without TMPRSS4 | 8e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 37, C 77. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRATD2]] | B | DAPP1 activity raises LRATD2's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.87× lower at baseline in the lines without DAPP1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[EPS8L1]] | B | DAPP1 activity raises EPS8L1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.43× lower at baseline in the lines without DAPP1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[OCLN]] | B | DAPP1 activity raises OCLN's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 6.26× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[KPNA7]] | B | DAPP1 activity raises KPNA7's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.73× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[PRRG4]] | B | DAPP1 activity raises PRRG4's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.60× lower at baseline in the lines without DAPP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[MYO6]] | B | DAPP1 activity raises MYO6's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without DAPP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[SLMAP]] | B | DAPP1 activity raises SLMAP's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 1.60× lower at baseline in the lines without DAPP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[PATJ]] | B | DAPP1 activity raises PATJ's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.05× lower at baseline in the lines without DAPP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[TNFRSF21]] | B | DAPP1 activity raises TNFRSF21's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.54× lower at baseline in the lines without DAPP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[ZNF165]] | B | DAPP1 activity raises ZNF165's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.44× lower at baseline in the lines without DAPP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[ELF3-AS1]] | B | DAPP1 activity raises ELF3-AS1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.22× lower at baseline in the lines without DAPP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[LGALS9]] | B | DAPP1 activity raises LGALS9's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.55× lower at baseline in the lines without DAPP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 57.6); signed map (56.0, 7.4). **Vector** length 61.8, 29.7% of its response variance represented; |z| ≥ 3 in 349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.3 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | +2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.9 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dual adaptor of phosphotyrosine and 3-phosphoinositides 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,816,827-99,870,190 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAM32 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Antigen activates B Cell Receptor (BCR) leading to generation of second messengers; Signaling by the B Cell Receptor (BCR); Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN19](https://www.uniprot.org/uniprotkb/Q9UN19) (Dual adapter for phosphotyrosine and 3-phosphotyrosine and 3-phosphoinositide):

> May act as a B-cell-associated adapter that regulates B-cell antigen receptor (BCR)-signaling downstream of PI3K.

**Summary**, from NCBI Gene [27071](https://www.ncbi.nlm.nih.gov/gene/27071):

> Enables phosphatidylinositol-3,4,5-trisphosphate binding activity and phosphatidylinositol-3,4-bisphosphate binding activity. Predicted to be involved in protein dephosphorylation and signal transduction. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16500) · Entrez [27071](https://www.ncbi.nlm.nih.gov/gene/27071) · UniProt [Q9UN19](https://www.uniprot.org/uniprotkb/Q9UN19) · Ensembl [ENSG00000070190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070190)

## Data

Gene col 942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 942); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 942]; `tensor/DDL_lfc|DDL_z.npy` [942]; `embed/gene_vectors.npy` [942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 942 or target_col == 942). Every well: [[DAPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
