---
symbol: "ARHGAP25"
type: "gene"
col: 8655
ensembl_id: "ENSG00000163219"
name: "Rho GTPase activating protein 25"
location: "2p13.3"
module: 27
arm: "+"
pooled_cpm: 4.74
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 27
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ARHGAP25

*Rho GTPase activating protein 25* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +13.9, q 3e-41, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -4.3, q 0.007, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMST]] (+0.78, fdr 7e-06), [[BMP5]] (+0.75, fdr 7e-06), [[LINC02466]] (+0.73, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[TNFRSF19]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MIR3667HG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +13.9 | 3e-41 | 5/18 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +12.6 | 3e-34 | 8/16 (SW48, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +8.1 | 1e-13 | 13/19 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.6 | 3e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +6.8 | 1e-09 | 8/19 (SW 900, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +4.7 | 2e-04 | 9/19 (NCI-H1792, SW480, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 3e-04 | 9/19 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.6 | 3e-04 | 1/9 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 9e-04 | 2/15 (SW48, NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 0.001 | 6/19 (NCI-H1792, A549, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.1 | 0.002 | 3/19 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +3.7 | 0.012 | 2/6 (HOP62, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.2 | 0.058 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.069 | 1/16 (A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -4.3 | 0.007 | 12/19 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.611×** | -4.2 | 0.007 | 5/19 (A549, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -3.6 | 0.051 | 13/20 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.6 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0917× (z -16.1) |
| [[SNU-1 (line)]] | wt | 160 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0638× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -8.9) |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0775× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.57 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0509× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.762 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMST]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BMP5]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02466]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[LINC01980]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[RUNX1T1]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[LINC00491]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ST18]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[POU6F2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[DACH1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GABRG2]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LINC01611]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PCSK1]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 6, C 21. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF19]] | B | TNFRSF19 activity raises ARHGAP25's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without TNFRSF19 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3 |
| [[SOX6]] | B | SOX6 activity raises ARHGAP25's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without SOX6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[DACH1]] | B | DACH1 activity raises ARHGAP25's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.58× lower at baseline in the lines without DACH1 | 0.049 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[FAM13C]] | B | FAM13C activity raises ARHGAP25's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without FAM13C | 0.056 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[POU3F2]] | B | POU3F2 activity raises ARHGAP25's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without POU3F2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[LINC00173]] | B | LINC00173 activity raises ARHGAP25's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without LINC00173 | 0.099 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[MIR3667HG]] | C | MIR3667HG activity raises ARHGAP25's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without MIR3667HG | 0.005 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises ARHGAP25's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without PHYHIPL | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises ARHGAP25's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.96× lower at baseline in the lines without POU6F2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises ARHGAP25's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.28× lower at baseline in the lines without PCSK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[ST18]] | C | ST18 activity raises ARHGAP25's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.03× lower at baseline in the lines without ST18 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises ARHGAP25's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.70× lower at baseline in the lines without CALCA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3667HG]] | C | ARHGAP25 activity raises MIR3667HG's level | lines that do not express ARHGAP25 (27) vs lines expressing it (23) | 2.84× lower at baseline in the lines without ARHGAP25 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC01967, MAGEB2, POU6F2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.5, 41.1); signed map (46.9, 34.4). **Vector** length 43.7, 9.53% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:68,679,601-68,826,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0053 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins |
| Reactome | 4 pathways, smallest: RAC1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P42331](https://www.uniprot.org/uniprotkb/P42331) (Rho GTPase-activating protein 25):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [9938](https://www.ncbi.nlm.nih.gov/gene/9938):

> ARHGAPs, such as ARHGAP25, encode negative regulators of Rho GTPases (see ARHA; MIM 165390), which are implicated in actin remodeling, cell polarity, and cell migration (Katoh and Katoh, 2004 [PubMed 15254788]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28951) · Entrez [9938](https://www.ncbi.nlm.nih.gov/gene/9938) · UniProt [P42331](https://www.uniprot.org/uniprotkb/P42331) · Ensembl [ENSG00000163219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163219)

## Data

Gene col 8655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8655); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8655]; `tensor/DDL_lfc|DDL_z.npy` [8655]; `embed/gene_vectors.npy` [8655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8655 or target_col == 8655). Every well: [[ARHGAP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
