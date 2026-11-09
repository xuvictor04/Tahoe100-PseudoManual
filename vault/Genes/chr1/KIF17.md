---
symbol: "KIF17"
type: "gene"
col: 3888
ensembl_id: "ENSG00000117245"
name: "kinesin family member 17"
location: "1p36.12"
module: 53
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/053", "written"]
generated_by: "tahoemap"
---

# KIF17

*kinesin family member 17* — 1p36.12

> [!summary] In one line
> KIF17 is a homodimeric kinesin-2 motor that carries cargo outward along microtubules in dendrites and into cilia.

## What it is

KIF17 is the vertebrate counterpart of *C. elegans* OSM-3: a processive, plus-end-directed homodimer, unlike heterotrimeric kinesin-II. Its best-established cargo is neuronal. The KIF17 tail binds the PDZ domain of mLin-10/Mint1, linking the motor to a scaffold carrying NMDA-receptor NR2B subunits, and this is the route by which NR2B-containing vesicles move into dendrites; CaMKII phosphorylation of the same region releases the cargo. A second, largely separate literature places KIF17 in cilia, where it enters the axoneme, associates with IFT-B, and is required for building photoreceptor outer segments. Mouse knockouts are viable, with impaired NR2B transport and memory deficits. Outside neurons and ciliated cells little is described.

## What is uncertain

Both of KIF17's established settings — dendrites and cilia — are largely absent from pooled cancer lines, so there is no known function here for a correlation to act through. The transcript is low in these lines, putting ambient RNA and mapping ambiguity across the conserved kinesin motor domain in play. Nothing in the literature connects KIF17 to p53 or to membrane repair, and nothing in this design separates a real association from one driven by a few lines.

## References

- Setou et al., 2000, Science — showed KIF17 transports NR2B-containing vesicles in dendrites via mLin-10/Mint1.
- Insinna et al., 2008, Developmental Biology — showed Kif17 is required for vertebrate photoreceptor outer-segment development.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.85× (z +20.8, q 0e+00, up in 28 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (C-33 A 0.0657×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.191×; ⚠ toxic; transcription drop); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0700×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE9]] (+0.81, fdr 7e-06), [[SELPLG]] (+0.81, fdr 7e-06), [[PITRM1-AS1]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00334]] → it (grade B ⚠); 5 go from it, the strongest it → [[PRKCG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.85×** | +20.8 | 0e+00 | 28/35 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +15.8 | 0e+00 | 28/30 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.65×** | +12.0 | 4e-31 | 30/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.56×** | +11.8 | 4e-30 | 22/30 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +9.6 | 8e-20 | 29/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +8.6 | 7e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +8.0 | 8e-14 | 21/37 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +6.6 | 3e-09 | 19/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.56×** | +6.2 | 4e-08 | 16/36 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +5.6 | 1e-06 | 1/15 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.3 | 6e-06 | 16/41 (SW480, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.76×** | +5.3 | 7e-06 | 10/36 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +4.9 | 4e-05 | 18/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.8 | 7e-05 | 10/41 (A498, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 1e-04 | 9/29 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 5 µM |  | **2.22×** | +3.9 | 0.004 | 2/25 (PANC-1, A498) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 9/41 (A498, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3888.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (C-33 A 0.0657×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.191×; ⚠ toxic; transcription drop); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0700×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.707× | -3.2 | 0.24 | 14/39 (C-33 A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.711× | -3.2 | 0.24 | 11/42 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.699× | -3.2 | 0.24 | 13/33 (HS-578T, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.716× | -3.1 | 0.24 | 8/41 (Panc 03.27, H4, …) | two highest doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | 0.796× | -3.0 | 0.27 | 4/42 (H4, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.60 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0657× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 2.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 3.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +8.5) | — |
| [[LoVo (line)]] | wt | 4.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 9.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 6.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE9]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.81 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.79 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[CHADL]] | +0.78 | +0.79 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MIR9-1HG]] | +0.78 | +0.77 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TMEM25]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CPT1C]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.76 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.76 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00334]] | B | LINC00334 activity raises KIF17's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without LINC00334 | 0.029 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[LAG3]] | B | LAG3 activity raises KIF17's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without LAG3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[NOTCH3]] | B | NOTCH3 activity raises KIF17's level | lines that do not express NOTCH3 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without NOTCH3 | 0.083 | ⚠ within organs, on part of the lines; also absent: WNT5B, GPR68, RNF150; maybe low, not absent |
| [[NPAS1]] | B | NPAS1 activity raises KIF17's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.70× lower at baseline in the lines without NPAS1 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCG]] | C | KIF17 activity raises PRKCG's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 2.97× lower at baseline in the lines without KIF17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |
| [[MYLK2]] | C | KIF17 activity raises MYLK2's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without KIF17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |
| [[TGIF2-RAB5IF]] | C | KIF17 activity raises TGIF2-RAB5IF's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without KIF17 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent |
| [[ITGA2B]] | C | KIF17 activity raises ITGA2B's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without KIF17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PTCH2]] | C | KIF17 activity raises PTCH2's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without KIF17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.1, -15.5); signed map (17.5, 12.6). **Vector** length 67.1, 10.8% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +20.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,664,014-20,718,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1405, KIF3X, KIF17B, OSM-3, KLP-2 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 9 pathways, smallest: Assembly and cell surface presentation of NMDA receptors; Intraflagellar transport; Activation of NMDA receptors and postsynaptic events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E2](https://www.uniprot.org/uniprotkb/Q9P2E2) (Kinesin-like protein KIF17):

> Together with RAB23 and IFT57, it is required for the localization of specific G protein-coupled receptors, such as dopamime receptor DRD1, to primary cilia. In association with the Apba1-containing complex (LIN-10-LIN-2-LIN-7 complex), transports vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules.

**Summary**, from NCBI Gene [57576](https://www.ncbi.nlm.nih.gov/gene/57576):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and plus-end-directed microtubule motor activity. Predicted to be involved in anterograde dendritic transport of neurotransmitter receptor complex. Predicted to act upstream of or within microtubule-based process; protein-containing complex localization; and vesicle-mediated transport. Predicted to be located in cytosol. Predicted to be part of kinesin complex. Predicted to be active in several cellular components, …

**Accessions** — [HGNC:19167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19167) · Entrez [57576](https://www.ncbi.nlm.nih.gov/gene/57576) · UniProt [Q9P2E2](https://www.uniprot.org/uniprotkb/Q9P2E2) · Ensembl [ENSG00000117245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117245)

## Data

Gene col 3888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3888); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3888]; `tensor/DDL_lfc|DDL_z.npy` [3888]; `embed/gene_vectors.npy` [3888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3888 or target_col == 3888). Every well: [[KIF17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/KIF17.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
