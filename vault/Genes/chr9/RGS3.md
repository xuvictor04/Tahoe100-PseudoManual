---
symbol: "RGS3"
type: "gene"
col: 6251
ensembl_id: "ENSG00000138835"
name: "regulator of G protein signaling 3"
location: "9q32"
module: 67
arm: "+"
pooled_cpm: 33.32
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# RGS3

*regulator of G protein signaling 3* — 9q32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.54×).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.570× (z -9.6, q 3e-19, down in 29 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNA2]] (+0.69, fdr 7e-06), [[TTK]] (+0.69, fdr 7e-06), [[CDCA3]] (+0.68, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PARPBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.54×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | 1.20× | +3.1 | 0.42 | 11/40 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.42 | 11/41 (PANC-1, KATO III, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.41× | +3.1 | 0.42 | 13/41 (SHP-77, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -9.6 | 3e-19 | 29/40 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -8.9 | 2e-16 | 28/40 (SNU-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -8.7 | 8e-16 | 26/41 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -8.6 | 1e-15 | 25/39 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -8.5 | 1e-15 | 24/41 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -8.1 | 3e-14 | 25/41 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -7.4 | 8e-12 | 23/40 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.629×** | -7.3 | 1e-11 | 24/37 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -7.3 | 2e-11 | 21/35 (HEC-1-A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -7.2 | 3e-11 | 26/41 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.744×** | -7.2 | 4e-11 | 28/41 (SNU-1, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.648×** | -7.0 | 1e-10 | 24/41 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.678×** | -6.7 | 1e-09 | 21/41 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.764×** | -6.5 | 3e-09 | 21/41 (A-427, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.789×** | -5.8 | 3e-07 | 23/41 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.796×** | -5.5 | 1e-06 | 21/41 (LS 180, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.799×** | -5.4 | 2e-06 | 21/40 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -5.4 | 3e-06 | 20/41 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.808×** | -5.1 | 7e-06 | 21/41 (HepG2/C3A, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.9 | 0.002 | 19/41 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.7 | 0.006 | 19/41 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.860× | -3.6 | 0.006 | 16/41 (Hs 766T, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 107 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -11.6) |
| [[SW480 (line)]] | alt | 52.5 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.353× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 17.0 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -13.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.5) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.236× (z -11.1) |
| [[COLO 205 (line)]] | alt | 52.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -16.8) |
| [[KATO III (line)]] | alt | 57.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.5) |
| [[SNU-1 (line)]] | wt | 48.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -16.5) |
| [[A-427 (line)]] | wt | 29.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.194× (z -14.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.258× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.0) |
| [[HCT15 (line)]] | alt | 60.6 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0686× (z -12.2) |
| [[HT-29 (line)]] | alt | 58.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.6) |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 27.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.1) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A549 (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.369× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[C32 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.437× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0788× (z -15.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -11.9) |
| [[SW48 (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.209× (z -9.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNA2]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TTK]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[FAM83D]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[NUF2]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ARHGEF39]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[INCENP]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[AURKB]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CDK1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CIT]] | +0.65 | +0.70 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RGS3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARPBP]] | B | RGS3 activity lowers PARPBP's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without RGS3 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NCAPH]] | B | RGS3 activity lowers NCAPH's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.92× higher at baseline in the lines without RGS3 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SGO2]] | B | RGS3 activity lowers SGO2's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without RGS3 | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.1, -55.4); signed map (-48.6, -41.0). **Vector** length 113, 29.2% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.57 to 12); *G2/M checkpoint* (hallmark, mean cos +0.56 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | +4.3 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -7.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -8.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,444,731-113,597,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C2PA, FLJ20370, PDZ-RGS3 |
| Gene groups (HGNC) | Regulators of G-protein signaling; C2 domain containing; PDZ domain containing |
| Reactome | 4 pathways, smallest: G alpha (q) signalling events; G alpha (i) signalling events; GPCR downstream signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P49796](https://www.uniprot.org/uniprotkb/P49796) (Regulator of G protein signaling 3):

> Down-regulates signaling from heterotrimeric G proteins by increasing the GTPase activity of the alpha subunits, thereby driving them into their inactive GDP-bound form. Down-regulates G protein-mediated release of inositol phosphates and activation of MAP kinases.

**Summary**, from NCBI Gene [5998](https://www.ncbi.nlm.nih.gov/gene/5998):

> This gene encodes a member of the regulator of G-protein signaling (RGS) family. This protein is a GTPase-activating protein that inhibits G-protein-mediated signal transduction. Alternative splicing and the use of alternative promoters results in multiple transcript variants encoding different isoforms. Long isoforms are largely cytosolic and plasma membrane-associated with a function in Wnt signaling and in the epithelial mesenchymal transition, while shorter N-terminally-truncated isoforms …

**Accessions** — [HGNC:9999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9999) · Entrez [5998](https://www.ncbi.nlm.nih.gov/gene/5998) · UniProt [P49796](https://www.uniprot.org/uniprotkb/P49796) · Ensembl [ENSG00000138835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138835)

## Data

Gene col 6251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6251); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6251]; `tensor/DDL_lfc|DDL_z.npy` [6251]; `embed/gene_vectors.npy` [6251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6251 or target_col == 6251). Every well: [[RGS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
