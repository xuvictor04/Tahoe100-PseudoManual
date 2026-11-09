---
symbol: "TWIST2"
type: "gene"
col: 13912
ensembl_id: "ENSG00000233608"
name: "twist family bHLH transcription factor 2"
location: "2q37.3"
module: 13
arm: "+"
pooled_cpm: 12.9
n_lines_expressing: 24
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 26
direction_downstream: 20
tags: ["gene", "module/013", "written"]
generated_by: "tahoemap"
---

# TWIST2

*twist family bHLH transcription factor 2* — 2q37.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TWIST2, cloned originally as Dermo-1, is a basic helix-loop-helix protein closely related to TWIST1 that acts in dermal and mesenchymal lineages and was characterised from the start as a repressor rather than an activator.

## What it is

TWIST2 shares TWIST1's bHLH domain almost residue for residue, dimerises with the same E proteins and binds the same E-boxes. It was isolated as Dermo-1 in a two-hybrid screen for E12 partners; notably, the original work found it bound E-boxes with E12 but had no detectable activation capacity, repressing myogenic bHLH proteins instead. Expression rises in embryonic and neonatal dermis and falls in adult tissue. Human genetics has been the most informative source since: biallelic loss of function underlies Setleis syndrome, a recessive focal facial dermal dysplasia, while recurrent missense substitutions at one conserved glutamate in the DNA-binding basic domain cause Ablepharon-macrostomia and Barber-Say syndromes — a change of function rather than a loss, with the particular substitution predicting which phenotype appears.

## What is uncertain

The main caveat is structural rather than biological: TWIST2's regulon overlaps TWIST1's by construction, so the adjacent high ranks are not independent support. Whether TWIST2 has outputs distinct from TWIST1 in any cell type remains partly open: the clean separations come from mouse expression domains and human syndromes, not distinct target sets. If the original characterisation as a repressor without intrinsic activation capacity holds, an activity convention that reads target expression as factor activity has the wrong sign for it. The Twist-box/p53 interaction was characterised for TWIST1; the twist box is conserved in TWIST2, but whether it does the same there is not established.

## References

- Li, Cserjesi & Olson, 1995, Developmental Biology — cloned Dermo-1 (TWIST2) as an E12 partner that binds E-boxes without detectable activation and represses myogenic bHLH proteins.
- Marchegiani et al., 2015, American Journal of Human Genetics — recurrent mutations in the basic domain of TWIST2 cause Ablepharon-macrostomia and Barber-Say syndromes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.85× (z +20.8, q 0e+00, up in 14 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.612× (z -6.9, q 3e-09, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSHZ3]] (+0.58, fdr 1e-05), [[FLI1]] (+0.57, fdr 1e-05), [[TSHZ3-AS1]] (+0.56, fdr 1e-05); moves opposite to [[VPS41]] (-0.47, fdr 1e-04), [[BABAM2]] (-0.46, fdr 4e-05), [[LINC01748]] (-0.44, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[MRC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +20.8 | 0e+00 | 14/20 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.5 | 6e-15 | 0/15 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.2 | 1e-10 | 4/20 (H4, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.4 | 2e-08 | 0/17 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +5.9 | 4e-07 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.5 | 8e-04 | 8/21 (A-172, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 4/21 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.005 | 4/21 (HOP62, A-427, …) | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.055 | 2/20 (RPMI-7951, HS-578T) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.056 | 1/21 (H4) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.063 | 2/19 (hTERT-HPNE, NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -6.9 | 3e-09 | 14/20 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.640×** | -6.0 | 3e-07 | 14/21 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.739×** | -6.0 | 3e-07 | 16/20 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -5.8 | 8e-07 | 10/21 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -5.7 | 1e-06 | 12/22 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -5.2 | 2e-05 | 17/22 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -5.0 | 4e-05 | 12/21 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.712×** | -4.8 | 1e-04 | 4/20 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.700×** | -4.6 | 2e-04 | 2/22 (HOP62, NCI-H661) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.733×** | -4.4 | 7e-04 | 10/21 (CHP-212, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.8 | 0.007 | 2/22 (HOP62, SW 1088) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.047 | 4/20 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.793×** | -3.3 | 0.047 | 12/21 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.641×** | -3.1 | 0.068 | 8/20 (HS-578T, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.0812× (z -25.1) |
| [[A-172 (line)]] | wt | 49.1 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0550× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.179× (z -20.8) |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -18.8) |
| [[A549 (line)]] | wt | 24.1 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.4) |
| [[HOP62 (line)]] | alt | 46.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.3) |
| [[H4 (line)]] | wt | 25.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 57.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.476× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.7) |
| [[PANC-1 (line)]] | alt | 5.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.5) | — |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FLI1]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TSHZ3-AS1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[EDNRA]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[BCL7A]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[BARX1]] | +0.54 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[GRAMD1B]] | +0.53 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SYNDIG1]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GDNF-AS1]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[EVC2]] | +0.51 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[ENG]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS41]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[BABAM2]] | -0.46 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[LINC01748]] | -0.44 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[NIHCOLE]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SPG11]] | -0.42 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PIGO]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 1, C 25. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TWIST2's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADAM12]] | C | ADAM12 activity raises TWIST2's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 6.04× lower at baseline in the lines without ADAM12 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[GJA1]] | C | GJA1 activity raises TWIST2's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 6.35× lower at baseline in the lines without GJA1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[CNRIP1]] | C | CNRIP1 activity raises TWIST2's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 5.93× lower at baseline in the lines without CNRIP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises TWIST2's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 5.91× lower at baseline in the lines without INSYN2B | 0.016 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[NDNF]] | C | NDNF activity raises TWIST2's level | lines that do not express NDNF (25) vs lines expressing it (25) | 5.49× lower at baseline in the lines without NDNF | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises TWIST2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.23× lower at baseline in the lines without PDGFRB | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[CYGB]] | C | CYGB activity raises TWIST2's level | lines that do not express CYGB (20) vs lines expressing it (30) | 4.39× lower at baseline in the lines without CYGB | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises TWIST2's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 4.28× lower at baseline in the lines without GDNF-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[FAM20C]] | C | FAM20C activity raises TWIST2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 4.46× lower at baseline in the lines without FAM20C | 0.028 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises TWIST2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.94× lower at baseline in the lines without LINC01411 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises TWIST2's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 4.09× lower at baseline in the lines without COL15A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 4, C 16. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRC2]] | B | TWIST2 activity raises MRC2's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.92× lower at baseline in the lines without TWIST2 | 0.050 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[SLC16A6]] | B | TWIST2 activity raises SLC16A6's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without TWIST2 | 0.052 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[GLIS3]] | B | TWIST2 activity raises GLIS3's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without TWIST2 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[BOC]] | B | TWIST2 activity raises BOC's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without TWIST2 | 0.093 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[TSHZ3]] | C | TWIST2 activity raises TSHZ3's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 6.66× lower at baseline in the lines without TWIST2 | 0.009 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[TSHZ3-AS1]] | C | TWIST2 activity raises TSHZ3-AS1's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.33× lower at baseline in the lines without TWIST2 | 0.029 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[WNT5B]] | C | TWIST2 activity raises WNT5B's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without TWIST2 | 0.039 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[ARHGAP22]] | C | TWIST2 activity raises ARHGAP22's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without TWIST2 | 0.046 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[GLIS1]] | C | TWIST2 activity raises GLIS1's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without TWIST2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[ARHGEF6]] | C | TWIST2 activity raises ARHGEF6's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without TWIST2 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[GJA1]] | C | TWIST2 activity raises GJA1's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 6.16× lower at baseline in the lines without TWIST2 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[WNT5A]] | C | TWIST2 activity raises WNT5A's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 4.42× lower at baseline in the lines without TWIST2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.7, 15.3); signed map (25.8, 49.8). **Vector** length 56.0, 13.7% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +20.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +5.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | -0.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | twist family bHLH transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,848,032-238,910,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DERMO1, Dermo-1, bHLHa39 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 10 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVJ9](https://www.uniprot.org/uniprotkb/Q8WVJ9) (Twist-related protein 2):

> Binds to the E-box consensus sequence 5'-CANNTG-3' as a heterodimer and inhibits transcriptional activation by MYOD1, MYOG, MEF2A and MEF2C. Also represses expression of pro-inflammatory cytokines such as TNFA and IL1B. Involved in postnatal glycogen storage and energy metabolism (By similarity). Inhibits the premature or ectopic differentiation of preosteoblast cells during osteogenesis, possibly by changing the internal signal transduction response of osteoblasts to external growth factors.

**Summary**, from NCBI Gene [117581](https://www.ncbi.nlm.nih.gov/gene/117581):

> The protein encoded by this gene is a basic helix-loop-helix type transcription factor and shares similarity with Twist. This protein may inhibit osteoblast maturation and maintain cells in a preosteoblast phenotype during osteoblast development. This gene may be upregulated in certain cancers. Mutations in this gene cause focal facial dermal dysplasia 3, Setleis type. Two transcript variants encoding the same protein have been found. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:20670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20670) · Entrez [117581](https://www.ncbi.nlm.nih.gov/gene/117581) · UniProt [Q8WVJ9](https://www.uniprot.org/uniprotkb/Q8WVJ9) · Ensembl [ENSG00000233608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233608)

## Data

Gene col 13912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13912); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13912]; `tensor/DDL_lfc|DDL_z.npy` [13912]; `embed/gene_vectors.npy` [13912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13912 or target_col == 13912). Every well: [[TWIST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TWIST2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
