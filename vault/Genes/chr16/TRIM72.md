---
symbol: "TRIM72"
type: "gene"
col: 10805
ensembl_id: "ENSG00000177238"
name: "tripartite motif containing 72"
location: "16p11.2"
module: 38
arm: "+"
pooled_cpm: 5.06
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 20
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# TRIM72

*tripartite motif containing 72* — 16p11.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TRIM72 encodes MG53, a striated-muscle E3 ubiquitin ligase that patches torn plasma membrane — a muscle gene that the earlier MG53/p53 study used as its exposure, measured as mRNA in cells that are not muscle.

## What it is

MG53 ("mitsugumin 53") is a tripartite-motif protein — a RING finger with E3 ubiquitin ligase activity, a B-box, an oligomerising coiled-coil and a C-terminal SPRY domain — expressed almost only in skeletal and cardiac muscle.

Its established job is acute membrane repair. When the sarcolemma tears, MG53 senses the change in redox environment, oligomerises, and nucleates a repair patch by drawing vesicles to the breach, alongside caveolin-3, dysferlin and PTRF/cavin-1. What brings it to the wound is the oxidative environment rather than calcium entry — calcium is still needed for the recruited vesicles to fuse — which separates its sensing step from the calcium-sensing dysferlin pathway. *Trim72*-null mice develop myopathy and tolerate ischaemia–reperfusion poorly, and recombinant MG53 protein is protective in injury models.

Two further activities matter here: the RING domain ubiquitinates the insulin receptor and IRS1, and MG53 restrains myoblast differentiation, entangling its expression with the muscle programme that produces it.

## What is uncertain

Nearly everything MG53 is known to do happens at the level of protein, localisation and ubiquitination, and this dataset has none of those: it measures mRNA, at one time point, with no knockdown, no overexpression and no protein readout. A null here constrains the mRNA-level association in these cells and cannot rule out a protein-level link.

Part of the measured signal is not this gene's transcript ([[Readthrough spillover]]). The strand-specific evidence that readthrough happens at this locus is solid, but the arithmetic over-predicts the observed rise, so the magnitude is unaccounted for and no clean subtraction exists. It also carries the largest plate batch gap in the dataset ([[Plate batch effects]]).

And two things the dataset cannot speak to: all 50 lines are TRIM72-wild-type and differ only in level, so nothing here contrasts functional with non-functional MG53; and the insulin-resistance role is genuinely disputed, groups disagreeing over whether circulating MG53 causes insulin resistance or merely marks muscle damage.

## References

- Cai et al., 2009, *Nature Cell Biology* — identified MG53 as the nucleating factor for acute membrane repair in striated muscle, with oligomerisation and recruitment driven by entry of the extracellular oxidative environment rather than by calcium.
- Song et al., 2013, *Nature* — MG53 as an E3 ligase for the insulin receptor and IRS1, with metabolic consequences on overexpression.
- Weisleder et al., 2012, *Science Translational Medicine* — recombinant MG53 delivered as a protein therapeutic in muscle injury models.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.2× (z +15.9, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.395× (z -4.2, q 0.015, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.94, fdr 7e-06), [[PYGM]] (+0.87, fdr 7e-06), [[PITRM1-AS1]] (+0.86, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MYOM1]] → it (grade B ⚠); 20 go from it, the strongest it → [[PITRM1-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.2×** | +15.9 | 0e+00 | 37/37 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **10.3×** | +14.8 | 0e+00 | 33/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.56×** | +8.4 | 7e-15 | 31/40 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.87×** | +7.9 | 3e-13 | 26/34 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **5.57×** | +7.4 | 2e-11 | 3/5 (HOP62, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.52×** | +6.5 | 8e-09 | 28/35 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.70×** | +5.9 | 4e-07 | 5/22 (HCT15, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.82×** | +5.5 | 2e-06 | 7/12 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.60×** | +5.5 | 2e-06 | 21/39 (A498, MIA PaCa-2, …) | top dose only | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +4.7 | 1e-04 | 18/31 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.05×** | +4.5 | 3e-04 | 15/43 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.70×** | +4.4 | 4e-04 | 23/43 (A498, NCI-H460, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +4.0 | 0.002 | 9/23 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.34×** | +3.8 | 0.006 | 19/44 (A498, HepG2/C3A, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.15×** | +3.4 | 0.024 | 12/40 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **2.12×** | +3.3 | 0.030 | 17/41 (RPMI-7951, J82, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.07×** | +3.1 | 0.068 | 6/41 (A-172, SW480, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.96×** | +3.0 | 0.080 | 6/41 (C32, C-33 A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.94×** | +2.9 | 0.090 | 9/41 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.395×** | -4.2 | 0.015 | 25/41 (SW 900, SNU-423, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | 0.607× | -3.2 | 0.31 | 11/43 (NCI-H2030, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.499× | -3.2 | 0.31 | 15/43 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.482× | -3.1 | 0.31 | 15/42 (LOX-IMVI, BT-474, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 1.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.3× (z +12.2) | — |
| [[A-172 (line)]] | wt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.5× (z +8.6) | — |
| [[A498 (line)]] | wt | 6.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +10.8) | — |
| [[C32 (line)]] | wt | 7.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 138× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.7× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 3.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +9.3) | — |
| [[LoVo (line)]] | wt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 43.3× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +8.6) | — |
| [[A-427 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.94 | +0.93 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.87 | +0.89 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.86 | +0.88 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LDHC]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.83 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MIR9-1HG]] | +0.83 | +0.82 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[IMPA1P1]] | +0.83 | +0.87 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[FGF18]] | +0.83 | +0.84 / +0.77 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.82 | +0.80 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOM1]] | B | MYOM1 activity raises TRIM72's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.63× lower at baseline in the lines without MYOM1 | 0.022 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TRIM72's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises TRIM72's level | lines that do not express F2 (11) vs lines expressing it (39) | 2.08× lower at baseline in the lines without F2 | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises TRIM72's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without LINC00334 | 0.038 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises TRIM72's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without LMO7DN | 0.055 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[ASGR1]] | B | ASGR1 activity raises TRIM72's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.86× lower at baseline in the lines without ASGR1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises TRIM72's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without IMPA1P1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises TRIM72's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.35× lower at baseline in the lines without NEK10 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises TRIM72's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without LINC02133 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PITRM1-AS1]] | C | TRIM72 activity raises PITRM1-AS1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without TRIM72 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[LINC01619]] | C | TRIM72 activity raises LINC01619's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without TRIM72 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[TMED6]] | C | TRIM72 activity raises TMED6's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without TRIM72 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[ALDH8A1]] | C | TRIM72 activity raises ALDH8A1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without TRIM72 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[NDFIP1]] | C | TRIM72 activity lowers NDFIP1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without TRIM72 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[ZDHHC11]] | C | TRIM72 activity raises ZDHHC11's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without TRIM72 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[HCLS1]] | C | TRIM72 activity raises HCLS1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without TRIM72 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[LINC01031]] | C | TRIM72 activity raises LINC01031's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without TRIM72 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[PPP1R10]] | C | TRIM72 activity raises PPP1R10's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without TRIM72 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[ADAM32]] | C | TRIM72 activity raises ADAM32's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without TRIM72 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[TEX29]] | C | TRIM72 activity raises TEX29's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without TRIM72 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[USP50]] | C | TRIM72 activity raises USP50's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without TRIM72 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, -16.2); signed map (16.2, 11.4). **Vector** length 97.9, 23.6% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +14.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.5 |
| fall | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 72 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,214,119-31,231,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MG53 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMU5](https://www.uniprot.org/uniprotkb/Q6ZMU5) (Tripartite motif-containing protein 72):

> Muscle-specific E3 ubiquitin-protein ligase that plays a central role in cell membrane repair by nucleating the assembly of the repair machinery at injury sites. Its ubiquitination activity is mediated by E2 ubiquitin-conjugating enzymes UBE2D1, UBE2D2 and UBE2D3 (By similarity). Acts as a sensor of oxidation: upon membrane damage, entry of extracellular oxidative environment results in disulfide bond formation and homooligomerization at the injury site (By similarity). This oligomerization …

**Summary**, from NCBI Gene [493829](https://www.ncbi.nlm.nih.gov/gene/493829):

> Enables identical protein binding activity. Predicted to be involved in several processes, including plasma membrane repair; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein homooligomerization. Predicted to act upstream of or within negative regulation of insulin receptor signaling pathway; negative regulation of insulin-like growth factor receptor signaling pathway; and negative regulation of myotube differentiation. Predicted to be located in cytoplasmic vesicle …

**Accessions** — [HGNC:32671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32671) · Entrez [493829](https://www.ncbi.nlm.nih.gov/gene/493829) · UniProt [Q6ZMU5](https://www.uniprot.org/uniprotkb/Q6ZMU5) · Ensembl [ENSG00000177238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177238)

## Data

Gene col 10805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10805); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10805]; `tensor/DDL_lfc|DDL_z.npy` [10805]; `embed/gene_vectors.npy` [10805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10805 or target_col == 10805). Every well: [[TRIM72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TRIM72.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
