---
symbol: "ELK4"
type: "gene"
col: 8183
ensembl_id: "ENSG00000158711"
name: "ETS transcription factor ELK4"
location: "1q32.1"
module: 3
arm: "-"
pooled_cpm: 78.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003", "written"]
generated_by: "tahoemap"
---

# ELK4

*ETS transcription factor ELK4* — 1q32.1

> [!summary] In one line
> ELK4 (SAP-1) is a ternary complex factor: an ETS-domain protein that docks onto DNA-bound SRF to carry growth-factor signals to serum response elements.

## What it is

ELK4 is one of three ternary complex factors, with ELK1 and ELK3, and was isolated as a protein recruited by serum response factor to the c-fos SRE; it cannot occupy its site unless SRF is bound: its B-box contacts the SRF dimer while its ETS domain contacts a GGA(A/T) motif beside the CArG box. ERK phosphorylation of C-terminal sites converts it into an activator, carrying mitogen signalling to immediate-early genes such as FOS and EGR1. The TCFs compete with the myocardin/MRTF family for the same surface on [[SRF]], switching it between mitogenic and cytoskeletal programmes. A recurrent SLC45A3-ELK4 chimeric transcript occurs in prostate cancer.

## What is uncertain

ELK4's curated target set is small and dominated by immediate-early transcripts, which move under nearly any perturbation, so an activity inferred from it across this compound panel may report generic stress. The score is not separable from ELK1 or SRF.

## References

- Dalton & Treisman, 1992, Cell — characterised SAP-1 as a protein recruited by serum response factor to the c-fos serum response element.
- Mo et al., 2001, Journal of Molecular Biology — crystal structure of a ternary SAP-1/SRF/c-fos SRE DNA complex.
- Rickman et al., 2009, Cancer Research — identified SLC45A3-ELK4 as a recurrent chimeric transcript in prostate cancer.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by the synergism of MyoD (or myogenin) with MEF2.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.53× (z +5.9, q 2e-06, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.644× (z -6.2, q 4e-07, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7C]] (+0.71, fdr 7e-06), [[PRKAR1A]] (+0.70, fdr 1e-05), [[RSC1A1]] (+0.69, fdr 7e-06); moves opposite to [[CWC15]] (-0.68, fdr 7e-06), [[ATP5MJ]] (-0.66, fdr 7e-05), [[DCTN6-DT]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SCRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +5.9 | 2e-06 | 35/48 (PANC-1, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.0 | 1e-04 | 29/48 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.0 | 1e-04 | 32/44 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 0.001 | 27/48 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.006 | 26/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.7 | 0.019 | 30/48 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.028 | 27/47 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.031 | 31/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.055 | 25/48 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.068 | 22/48 (A-172, J82, …) | inconsistent across doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.11 | 19/48 (J82, A-427, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.24× | +3.0 | 0.13 | 22/49 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -6.2 | 4e-07 | 42/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -5.9 | 9e-07 | 43/49 (AN3 CA, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -5.5 | 5e-06 | 42/48 (A498, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.703×** | -4.9 | 1e-04 | 34/48 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -4.9 | 1e-04 | 38/48 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -4.5 | 8e-04 | 3/50 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.732×** | -4.4 | 1e-03 | 29/48 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.037 | 24/48 (NCI-H1573, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -3.3 | 0.052 | 23/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.13 | 17/48 (RKO, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[A498 (line)]] | wt | 106 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.432× (z -8.8) |
| [[AN3 CA (line)]] | alt | 62.1 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0436× (z -8.8) |
| [[C32 (line)]] | wt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.104× (z -8.5) |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 92.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.333× (z -10.3) |
| [[SW 1271 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0849× (z -10.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[PRKAR1A]] | +0.70 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[RSC1A1]] | +0.69 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[CHRAC1]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RBM12]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PSME3]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[KLC2]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.66 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[HDHD2]] | +0.65 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RNASEH1]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.64 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[MSANTD7]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC15]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.66 | -0.38 / -0.69 | both halves | 7e-05 |  |
| [[DCTN6-DT]] | -0.65 | -0.43 / -0.73 | both halves | 3e-05 |  |
| [[MALSU1]] | -0.64 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[RAC3]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[SEZ6L2]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[A1BG]] | -0.62 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[FAM182B]] | -0.62 | -0.37 / -0.75 | both halves | 9e-05 |  |
| [[PHAF1]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MARCHF9]] | -0.62 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[RAB40C]] | -0.62 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[RPS26]] | -0.62 | -0.26 / -0.66 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCRN1]] | B | SCRN1 activity lowers ELK4's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.29× higher at baseline in the lines without SCRN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |
| [[HDAC6]] | B | HDAC6 activity raises ELK4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRDM5]] | B | PRDM5 activity raises ELK4's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without PRDM5 | 0.096 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.0, -22.1); signed map (17.6, -33.7). **Vector** length 123, 36.2% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +2.6 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.5 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ETS transcription factor ELK4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,597,556-205,632,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP1 |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [P28324](https://www.uniprot.org/uniprotkb/P28324) (ETS domain-containing protein Elk-4):

> Involved in both transcriptional activation and repression. Interaction with SIRT7 leads to recruitment and stabilization of SIRT7 at promoters, followed by deacetylation of histone H3 at 'Lys-18' (H3K18Ac) and subsequent transcription repression. Forms a ternary complex with the serum response factor (SRF). Requires DNA-bound SRF for ternary complex formation and makes extensive DNA contacts to the 5'side of SRF, but does not bind DNA autonomously.

**Summary**, from NCBI Gene [2005](https://www.ncbi.nlm.nih.gov/gene/2005):

> This gene is a member of the Ets family of transcription factors and of the ternary complex factor (TCF) subfamily. Proteins of the TCF subfamily form a ternary complex by binding to the the serum response factor and the serum reponse element in the promoter of the c-fos proto-oncogene. The protein encoded by this gene is phosphorylated by the kinases, MAPK1 and MAPK8. Several transcript variants have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3326) · Entrez [2005](https://www.ncbi.nlm.nih.gov/gene/2005) · UniProt [P28324](https://www.uniprot.org/uniprotkb/P28324) · Ensembl [ENSG00000158711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158711)

## Data

Gene col 8183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8183); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8183]; `tensor/DDL_lfc|DDL_z.npy` [8183]; `embed/gene_vectors.npy` [8183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8183 or target_col == 8183). Every well: [[ELK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ELK4.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
