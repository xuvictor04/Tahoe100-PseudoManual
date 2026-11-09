---
symbol: "SELPLG"
type: "gene"
col: 3173
ensembl_id: "ENSG00000110876"
name: "selectin P ligand"
location: "12q24.11"
module: 39
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039", "written"]
generated_by: "tahoemap"
---

# SELPLG

*selectin P ligand* — 12q24.11

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SELPLG encodes PSGL-1 (CD162), the leukocyte sialomucin that is the principal ligand for P-selectin and lets circulating leukocytes tether and roll on activated endothelium.

## What it is

PSGL-1 is a disulfide-linked homodimeric mucin whose function depends almost entirely on post-translational decoration: high-affinity P-selectin binding needs core-2 O-glycans carrying sialyl-Lewis-x, built by the fucosyltransferase FUT7, together with sulfated tyrosines near the N-terminus. It is expressed on most leukocyte lineages, also binds E- and L-selectin, and PSGL-1-deficient mice show defective P-selectin-dependent neutrophil rolling and recruitment. Beyond adhesion it signals inward, contributing to mechanotransduction and integrin activation, and it has a second identity in immune regulation: VISTA was identified as an acidic-pH-selective ligand for PSGL-1, making the pair a candidate checkpoint operating specifically in the acidic tumour microenvironment.

## What is uncertain

Nearly all of it. SELPLG carries the readthrough-geometry flag: it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so a share of the reads credited to SELPLG may be transcriptional readthrough rather than its own output ([[Readthrough spillover]]). In the earlier MG53/p53 study it tracked measured MG53, which is vulnerable to exactly this, so that correlation was as easily a shared artefact of how both are quantified as it was biology; no mechanism connects selectin-mediated adhesion to MG53. Read any partner of SELPLG the same way until an orthogonal, locus-aware assay says otherwise.

## References

- Sako et al., 1993, Cell — expression-cloned PSGL-1 as a functional glycoprotein ligand for P-selectin.
- Pouyani & Seed, 1995, Cell — showed that PSGL-1 recognition by P-selectin requires N-terminal tyrosine sulfation alongside its O-glycan.
- Yang et al., 1999, Journal of Experimental Medicine — PSGL-1-null mice are defective in P-selectin-mediated neutrophil rolling and migration.
- Johnston et al., 2019, Nature — identified VISTA as an acidic-pH-selective ligand for PSGL-1 that suppresses T cells.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.21× (z +12.6, q 1e-33, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.487× (z -4.2, q 0.013, down in 10 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0850×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.88, fdr 7e-06), [[TRIM72]] (+0.83, fdr 7e-06), [[MPP4]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[C9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.21×** | +12.6 | 1e-33 | 26/31 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.51×** | +9.3 | 3e-18 | 26/35 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.45×** | +9.3 | 4e-18 | 22/29 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +9.1 | 1e-17 | 24/30 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.11×** | +8.1 | 7e-14 | 2/4 (A498, AsPC-1) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.55×** | +7.5 | 4e-12 | 1/2 (HOP62) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +7.4 | 1e-11 | 16/26 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +6.7 | 1e-09 | 19/30 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.56×** | +5.8 | 4e-07 | 25/43 (A498, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +5.6 | 1e-06 | 18/40 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.37×** | +5.3 | 5e-06 | 3/14 (SW 900, NCI-H2030, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +5.0 | 2e-05 | 16/36 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.9 | 4e-05 | 4/15 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.10×** | +4.6 | 2e-04 | 17/43 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.004 | 10/39 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.004 | 11/42 (HOP62, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.84×** | +3.6 | 0.009 | 11/37 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.77×** | +3.5 | 0.012 | 10/43 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.82×** | +3.5 | 0.014 | 5/34 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.3 | 0.021 | 9/34 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3173.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0850×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.487×** | -4.2 | 0.013 | 10/31 (C32, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.489× | -3.5 | 0.12 | 16/38 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.607× | -3.1 | 0.34 | 13/37 (NCI-H1792, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.04 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0850× (z -9.1) |
| [[A-172 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.878 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.693 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.83 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MPP4]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[USP50]] | +0.82 | +0.86 / +0.80 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.82 | +0.81 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.82 | +0.84 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ALDH8A1]] | +0.81 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[KIF17]] | +0.81 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.81 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.80 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[OIT3]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C9]] | B | C9 activity raises SELPLG's level | lines that do not express C9 (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without C9 | 0.011 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |
| [[TOP2A]] | B | TOP2A activity lowers SELPLG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DGKI]] | B | DGKI activity raises SELPLG's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without DGKI | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises SELPLG's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without IMPA1P1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[LINC01291]] | B | LINC01291 activity raises SELPLG's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without LINC01291 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -15.3); signed map (17.1, 11.2). **Vector** length 76.7, 14.2% of its response variance represented; |z| ≥ 3 in 1,199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +9.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | selectin P ligand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:108,621,895-108,633,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSGL-1, CD162 |
| Gene groups (HGNC) | CD molecules; Receptor ligands |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14242](https://www.uniprot.org/uniprotkb/Q14242) (P-selectin glycoprotein ligand 1):

> A SLe(x)-type proteoglycan, which through high affinity, calcium-dependent interactions with E-, P- and L-selectins, mediates rapid rolling of leukocytes over vascular surfaces during the initial steps in inflammation. Critical for the initial leukocyte capture.; (Microbial infection) Acts as a receptor for enterovirus 71.

**Summary**, from NCBI Gene [6404](https://www.ncbi.nlm.nih.gov/gene/6404):

> This gene encodes a glycoprotein that functions as a high affinity counter-receptor for the cell adhesion molecules P-, E- and L- selectin expressed on myeloid cells and stimulated T lymphocytes. As such, this protein plays a critical role in leukocyte trafficking during inflammation by tethering of leukocytes to activated platelets or endothelia expressing selectins. This protein requires two post-translational modifications, tyrosine sulfation and the addition of the sialyl Lewis x …

**Accessions** — [HGNC:10722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10722) · Entrez [6404](https://www.ncbi.nlm.nih.gov/gene/6404) · UniProt [Q14242](https://www.uniprot.org/uniprotkb/Q14242) · Ensembl [ENSG00000110876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110876)

## Data

Gene col 3173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3173); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3173]; `tensor/DDL_lfc|DDL_z.npy` [3173]; `embed/gene_vectors.npy` [3173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3173 or target_col == 3173). Every well: [[SELPLG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SELPLG.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
