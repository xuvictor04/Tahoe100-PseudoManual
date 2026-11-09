---
symbol: "GRAMD2A"
type: "gene"
col: 10594
ensembl_id: "ENSG00000175318"
name: "GRAM domain containing 2A"
location: "15q23"
module: 53
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/053", "written"]
generated_by: "tahoemap"
---

# GRAMD2A

*GRAM domain containing 2A* — 15q23

> [!summary] In one line
> GRAMD2A encodes a tail-anchored ER protein reported to tether the endoplasmic reticulum to PI(4,5)P2-rich patches of the plasma membrane, and nearly all of what is known about it comes from one study.

## What it is

GRAMD2A, formerly GRAMD2, sits at 15q23. Its product is anchored in the ER membrane and presents a cytosolic GRAM domain that binds PI(4,5)P2, and that preference confines it to a subset of ER-plasma-membrane contact sites distinct from those held by the GRAMD1/Aster sterol transporters, alongside the extended synaptotagmins E-Syt2 and E-Syt3. The same work proposed it pre-marks the sites where STIM1 accumulates during store-operated calcium entry, making it an organiser of contact-site identity rather than a transporter. Its kinship to the yeast Lam/Ltc sterol-transfer proteins is domain homology only; no transfer activity has been shown, there is no animal knockout, and expression is low and uneven.

## What is uncertain

This is effectively a one-paper gene, and that paper's most interesting claim is its least settled: reviewers noted roughly half of STIM1 puncta formed at sites GRAMD2A did not mark. Antibody staining in the Human Protein Atlas puts the protein in nucleoli and nuclear speckles, irreconcilable with a tail-anchored ER tether; one localisation is wrong, most likely the antibody's. Nothing links the gene to p53, and at the level seen here ambient RNA stays a live explanation.

## References

- Besprozvannaya et al., 2018, eLife — showed GRAMD2a marks a PI(4,5)P2-dependent subset of ER-PM contact sites distinct from GRAMD1a's, and proposed a role in STIM1 recruitment.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.41× (z +16.7, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDHC]] (+0.84, fdr 7e-06), [[TRIM72]] (+0.82, fdr 7e-06), [[AZU1]] (+0.82, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.41×** | +16.7 | 0e+00 | 23/24 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.71×** | +15.4 | 0e+00 | 20/28 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.95×** | +9.3 | 4e-18 | 1/3 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.73×** | +9.2 | 4e-18 | 19/31 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.19×** | +8.1 | 6e-14 | 26/41 (NCI-H2030, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.83×** | +6.7 | 2e-09 | 1/3 (HEC-1-A) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +6.3 | 3e-08 | 14/28 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +4.9 | 6e-05 | 14/37 (A498, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.98×** | +4.8 | 1e-04 | 2/8 (PANC-1, HOP62) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.94×** | +4.6 | 2e-04 | 12/37 (PANC-1, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.89×** | +4.3 | 0.001 | 0/7 | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.001 | 4/39 (A498, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +4.1 | 0.002 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.82×** | +4.0 | 0.002 | 6/19 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.003 | 9/27 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +3.6 | 0.009 | 8/41 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.6 | 0.009 | 7/28 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.026 | 6/44 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +2.9 | 0.090 | 3/35 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10594.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.0444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.652× | -3.0 | 0.97 | 7/40 (HT-29, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 113× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0444× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 3.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 0.689 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.655 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.852 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.986 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.831 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.857 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.569 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.650 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.602 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHC]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.82 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[AZU1]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.81 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.80 | +0.73 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.80 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R36]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[KIF17]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SEMA4A]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRAMD2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ATAD3C]] | B | ATAD3C activity raises GRAMD2A's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.38× lower at baseline in the lines without ATAD3C | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[F2]] | B | F2 activity raises GRAMD2A's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without F2 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises GRAMD2A's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without PTPN6 | 0.061 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[LINC01291]] | B | LINC01291 activity raises GRAMD2A's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without LINC01291 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[ITGB2]] | B | ITGB2 activity raises GRAMD2A's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.25× lower at baseline in the lines without ITGB2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.1, -16.1); signed map (16.8, 12.5). **Vector** length 55.3, 9.22% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +3.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -1.5 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,159,806-72,197,787 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GRAMD2 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUY3](https://www.uniprot.org/uniprotkb/Q8IUY3) (GRAM domain-containing protein 2A):

> Participates in the organization of endoplasmic reticulum-plasma membrane contact sites (EPCS) with pleiotropic functions including STIM1 recruitment and calcium homeostasis. Constitutive tether that co-localizes with ESYT2/3 tethers at endoplasmic reticulum-plasma membrane contact sites in a phosphatidylinositol lipid-dependent manner. Pre-marks the subset of phosphatidylinositol 4,5-biphosphate (PI(4,5)P2)-enriched EPCS destined for the store-operated calcium entry pathway (SOCE).

**Summary**, from NCBI Gene [196996](https://www.ncbi.nlm.nih.gov/gene/196996):

> Enables phosphatidylinositol binding activity and phosphatidylinositol-4,5-bisphosphate binding activity. Involved in endoplasmic reticulum-plasma membrane tethering and regulation of store-operated calcium entry. Located in endoplasmic reticulum membrane; organelle membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27287) · Entrez [196996](https://www.ncbi.nlm.nih.gov/gene/196996) · UniProt [Q8IUY3](https://www.uniprot.org/uniprotkb/Q8IUY3) · Ensembl [ENSG00000175318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175318)

## Data

Gene col 10594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10594); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10594]; `tensor/DDL_lfc|DDL_z.npy` [10594]; `embed/gene_vectors.npy` [10594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10594 or target_col == 10594). Every well: [[GRAMD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/GRAMD2A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
