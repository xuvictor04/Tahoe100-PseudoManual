---
symbol: "PHLDA3"
type: "gene"
col: 10483
ensembl_id: "ENSG00000174307"
name: "pleckstrin homology like domain family A member 3"
location: "1q32.1"
module: 62
arm: "+"
pooled_cpm: 13.36
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# PHLDA3

*pleckstrin homology like domain family A member 3* — 1q32.1

> [!summary] In one line
> PHLDA3 encodes a small PH-domain-only protein that p53 induces to compete AKT off the membrane — one of the few routes by which p53's transcriptional output reaches into PI3K signalling.

## What it is

PHLDA3 is about as minimal as a signalling protein gets: roughly 127 residues, essentially a single pleckstrin homology domain, with no catalytic activity and no other recognisable module. The proposed mechanism follows from that architecture. The PH domain binds membrane phosphoinositides and competes with AKT's own PH domain for them, blocking AKT's recruitment to the plasma membrane and so its activating phosphorylation by PDK1 and mTORC2. The consequence is reduced AKT output: less mTORC1 signalling, less FOXO inhibition, less of the survival signalling AKT normally supplies. It works by occupancy rather than catalysis, so the effect is competitive: it scales with how much PHLDA3 is present.

PHLDA3 is a direct p53 target. p53 binds a response element at the locus and the gene is induced on DNA damage, placing it among the p53 outputs that act on signalling rather than on the cycle, the mitochondrion or repair. Its best-developed disease role is in neuroendocrine tumours: the locus undergoes loss of heterozygosity at high frequency in pancreatic neuroendocrine tumours, with promoter methylation as a plausible second hit; the LOH is reported to be mutually exclusive with p53 loss, which is the argument that PHLDA3 is a principal downstream mediator of p53 in that lineage; Phlda3-deficient mice develop islet hyperplasia, and PHLDA3 loss cooperates with Men1 loss.

## What is uncertain

That PHLDA3 is p53-inducible is well established. How much of the AKT inhibition attributed to it operates at endogenous expression levels, outside the overexpression and knockdown systems where it was characterised, is a weaker claim, and whether phosphoinositide competition is the whole mechanism — rather than one component alongside unmapped partners — is unsettled. The tumour-suppressor evidence is lineage-concentrated: strong for neuroendocrine tumours, an extrapolation elsewhere, and much of the functional literature comes from one group, so independent replication is thinner than the coherence of the story suggests. Two cautions apply here. PHLDA3 has reported hypoxia- and other stress-responsive inputs, so induction under a drug exposure is not by itself evidence that p53 did it; and the gene carries a mixed-direction flag in the study's own tables, meaning its behaviour across compounds is not uniform — a reason to treat it as a corroborating member of the programme rather than a readout in its own right.

## References

- Kawase et al., 2009, Cell — identified PHLDA3 as a p53-regulated PH-only protein that represses AKT by blocking its membrane translocation.
- Ohki et al., 2014, PNAS — PHLDA3 is a tumour suppressor of pancreatic neuroendocrine tumours, with frequent LOH, islet hyperplasia in deficient mice, and cooperation with Men1 loss.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.19× (z +4.3, q 0.009, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.214× (z -16.3, q 0e+00, down in 35 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS27L]] (+0.73, fdr 7e-06), [[TP53INP1]] (+0.71, fdr 8e-06), [[CES2]] (+0.70, fdr 1e-05); moves opposite to [[SRPK1]] (-0.48, fdr 3e-05), [[RRM2]] (-0.46, fdr 4e-05), [[GART]] (-0.46, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 3 go from it, the strongest it → [[GART]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +4.3 | 0.009 | 18/40 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.027 | 12/40 (LOX-IMVI, HOP62, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.7 | 0.047 | 2/40 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.047 | 13/39 (A-172, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.37× | +3.2 | 0.17 | 13/33 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.214×** | -16.3 | 0e+00 | 35/39 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.243×** | -14.9 | 0e+00 | 35/39 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.292×** | -13.0 | 2e-36 | 36/39 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -9.1 | 1e-17 | 22/37 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -8.1 | 5e-14 | 22/38 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -8.0 | 2e-13 | 23/39 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.476×** | -7.8 | 4e-13 | 29/39 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -5.9 | 2e-07 | 22/39 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -5.1 | 2e-05 | 21/39 (LoVo, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.9 | 5e-05 | 19/39 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.466×** | -4.2 | 0.001 | 13/40 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -3.9 | 0.005 | 17/38 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.8 | 0.006 | 14/39 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -3.8 | 0.007 | 16/39 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.706×** | -3.7 | 0.009 | 15/39 (HOP62, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.708×** | -3.6 | 0.009 | 9/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 40.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -15.1) |
| [[A-172 (line)]] | wt | 50.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0947× (z -16.2) |
| [[C32 (line)]] | wt | 35.1 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.60× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.93× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -12.3) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 17.8 | 1 (1 ⚠) | 3 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.47× (z +9.1) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -10.3) |
| [[SW48 (line)]] | wt | 20.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0781× (z -11.4) |
| [[A498 (line)]] | wt | 37.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -17.3) |
| [[A549 (line)]] | wt | 17.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 8.46 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.0) |
| [[LoVo (line)]] | wt | 23.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0317× (z -26.0) |
| [[LOX-IMVI (line)]] | wt | 22.1 | 1 | 2 | [[Selinexor (drug)]] 5 µM 3.15× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.142× (z -10.3) |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -12.0) |
| [[SW480 (line)]] | alt | 7.47 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -10.6) |
| [[HOP62 (line)]] | alt | 9.04 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.2) |
| [[SW 900 (line)]] | alt | 9.03 | 0 | 2 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0430× (z -10.8) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0608× (z -12.3) |
| [[COLO 205 (line)]] | alt | 6.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0579× (z -8.6) |
| [[H4 (line)]] | wt | 18.4 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0760× (z -10.0) |
| [[HT-29 (line)]] | alt | 7.25 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0769× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -8.9) |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS27L]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[TP53INP1]] | +0.71 | +0.58 / +0.73 | both halves | 8e-06 | **novel candidate** |
| [[CES2]] | +0.70 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[PINCR]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[MDM2]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 473 |
| [[BLOC1S2]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[FDXR]] | +0.68 | +0.49 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 471 |
| [[BAX]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ZMAT3]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 564 |
| [[ABCA12]] | +0.66 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ZNF79]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[PURPL]] | +0.65 | +0.44 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK1]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RRM2]] | -0.46 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[GART]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CBX3]] | -0.45 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity strengthens PHLDA3's drug response | lines that do not express PINCR (22) vs lines expressing it (18) | the lines without PINCR respond 0.82× as strongly (z diff +0.61); strongest at Panobinostat 5 µM: 0.37x vs 0.15x (z diff +4.2) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[PINCR]] | B | PINCR activity raises PHLDA3's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without PINCR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PTCHD4]] | B | PTCHD4 activity raises PHLDA3's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without PTCHD4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[MIR34AHG]] | B | MIR34AHG activity raises PHLDA3's level | lines that do not express MIR34AHG (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without MIR34AHG | 0.046 | ⚠ within organs, on part of the lines; also absent: SPATA18, LINC01876 |
| [[TP53]] | B | TP53 activity strengthens PHLDA3's drug response | recorded loss-of-function mutation of TP53 in 23 lines vs 17 not recorded | the TP53-altered lines respond 0.94× as strongly (z diff +0.20); strongest at Panobinostat 5 µM: 0.34x vs 0.15x (z diff +3.7) | 0.065 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GART]] | B | PHLDA3 activity lowers GART's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without PHLDA3 | 0.043 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |
| [[SRPK1]] | B | PHLDA3 activity lowers SRPK1's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without PHLDA3 | 0.062 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |
| [[BMP1]] | B | PHLDA3 activity raises BMP1's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.95× lower at baseline in the lines without PHLDA3 | 0.088 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, 36.1); signed map (42.0, -24.0). **Vector** length 99.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.60 to 6); *apoptosis* (hallmark, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.9 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -13.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -5.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,464,278-201,469,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIH1 |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5J5](https://www.uniprot.org/uniprotkb/Q9Y5J5) (Pleckstrin homology-like domain family A member 3):

> p53/TP53-regulated repressor of Akt/AKT1 signaling. Represses AKT1 by preventing AKT1-binding to membrane lipids, thereby inhibiting AKT1 translocation to the cellular membrane and activation. Contributes to p53/TP53-dependent apoptosis by repressing AKT1 activity. Its direct transcription regulation by p53/TP53 may explain how p53/TP53 can negatively regulate AKT1. May act as a tumor suppressor.

**Summary**, from NCBI Gene [23612](https://www.ncbi.nlm.nih.gov/gene/23612):

> Enables phosphatidylinositol phosphate binding activity and phosphatidylinositol-3,4-bisphosphate binding activity. Involved in intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator; negative regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and positive regulation of apoptotic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8934) · Entrez [23612](https://www.ncbi.nlm.nih.gov/gene/23612) · UniProt [Q9Y5J5](https://www.uniprot.org/uniprotkb/Q9Y5J5) · Ensembl [ENSG00000174307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174307)

## Data

Gene col 10483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10483); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10483]; `tensor/DDL_lfc|DDL_z.npy` [10483]; `embed/gene_vectors.npy` [10483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10483 or target_col == 10483). Every well: [[PHLDA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PHLDA3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
