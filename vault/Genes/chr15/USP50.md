---
symbol: "USP50"
type: "gene"
col: 9918
ensembl_id: "ENSG00000170236"
name: "ubiquitin specific peptidase 50"
location: "15q21.1"
module: 39
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# USP50

*ubiquitin specific peptidase 50* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.78× (z +21.4, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.435× (z -4.2, q 0.014, down in 12 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.89, fdr 7e-06), [[SLC6A13]] (+0.87, fdr 7e-06), [[ALDH8A1]] (+0.87, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SLC26A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.78×** | +21.4 | 0e+00 | 37/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +12.5 | 2e-33 | 34/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +11.5 | 3e-28 | 6/12 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +9.3 | 2e-18 | 18/27 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +8.6 | 7e-16 | 28/39 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +8.3 | 7e-15 | 28/45 (HT-29, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +6.3 | 2e-08 | 24/45 (J82, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.0 | 1e-07 | 19/39 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.3 | 7e-06 | 6/19 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +5.1 | 2e-05 | 21/44 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 13/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.4 | 4e-04 | 16/37 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.006 | 11/45 (SW480, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +3.0 | 0.099 | 6/44 (CFPAC-1, SNU-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.435×** | -4.2 | 0.014 | 12/37 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.657×** | -3.9 | 0.033 | 12/43 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.080 | 11/45 (SHP-77, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.709× | -3.2 | 0.16 | 14/45 (NCI-H23, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.720× | -3.2 | 0.16 | 14/45 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.31 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0774× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[NCI-H460 (line)]] | wt | 4.33 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +18.2) | [[Canagliflozin (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[J82 (line)]] | alt | 8.53 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +8.7) | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0725× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +11.0) | [[Belumosudil (drug)]] 5 µM 0.0696× (z -10.5) |
| [[A-172 (line)]] | wt | 4.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +10.0) | — |
| [[A549 (line)]] | wt | 6.71 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.102× (z -9.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 4.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 4.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 8.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +8.9) | — |
| [[KATO III (line)]] | alt | 4.93 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0640× (z -9.6) |
| [[LoVo (line)]] | wt | 8.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 7.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 4.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.4) | — |
| [[A-427 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.89 | +0.89 / +0.82 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.87 | +0.90 / +0.80 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.87 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[DPYS]] | +0.86 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.85 | +0.86 / +0.80 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.85 | +0.88 / +0.72 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.84 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | SLC26A4 activity raises USP50's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without SLC26A4 | 0.015 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[AOX1]] | B | AOX1 activity raises USP50's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.44× lower at baseline in the lines without AOX1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[C12orf50]] | B | C12orf50 activity raises USP50's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without C12orf50 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[APH1B]] | B | APH1B activity raises USP50's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without APH1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[DYSF]] | B | DYSF activity raises USP50's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without DYSF | 0.043 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises USP50's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without ASGR1 | 0.052 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[MYOM1]] | B | MYOM1 activity raises USP50's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without MYOM1 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers USP50's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02133]] | C | LINC02133 activity raises USP50's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without LINC02133 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |
| [[MPP4]] | C | MPP4 activity raises USP50's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity raises USP50's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without TRIM72 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[MMP25]] | C | MMP25 activity raises USP50's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.57× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.923). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.5, -13.6); signed map (18.2, 9.1). **Vector** length 84.4, 15.7% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +21.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +8.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:50,494,018-50,546,708 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70EL3](https://www.uniprot.org/uniprotkb/Q70EL3) (Ubiquitin carboxyl-terminal hydrolase 50):

> Deubiquitinating enzyme that removes conjugated ubiquitin from specific proteins to regulate different cellular processes. Regulates the inflammasome signaling pathway by deubiquitinating 'Lys-63'-linked polyubiquitination of the PYCARD/ASC adapter protein. Regulates the ubiquitination and stability of the ACE2 protein. Acts as a negative regulator of the G2/M checkpoint pathway, by preventing serine/threonine kinase WEE1 degradation, thereby repressing entry into mitosis following activation …

**Summary**, from NCBI Gene [373509](https://www.ncbi.nlm.nih.gov/gene/373509):

> Enables cysteine-type deubiquitinase activity. Involved in regulation of cell cycle G2/M phase transition. Acts upstream of or within several processes, including nuclear speck organization; positive regulation of NLRP3 inflammasome complex assembly; and positive regulation of interleukin-1 beta production. Located in centrosome; cytoplasm; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20079) · Entrez [373509](https://www.ncbi.nlm.nih.gov/gene/373509) · UniProt [Q70EL3](https://www.uniprot.org/uniprotkb/Q70EL3) · Ensembl [ENSG00000170236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170236)

## Data

Gene col 9918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9918); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9918]; `tensor/DDL_lfc|DDL_z.npy` [9918]; `embed/gene_vectors.npy` [9918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9918 or target_col == 9918). Every well: [[USP50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
