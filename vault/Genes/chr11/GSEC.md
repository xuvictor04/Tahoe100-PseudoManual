---
symbol: "GSEC"
type: "gene"
col: 15969
ensembl_id: "ENSG00000280832"
name: "G-quadruplex forming sequence containing lncRNA"
location: "11q24.2"
module: 109
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# GSEC

*G-quadruplex forming sequence containing lncRNA* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +6.8, q 5e-09, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.76× (z +4.9, q 2e-04, up in 8 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.493× (z -6.2, q 4e-07, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A5]] (+0.53, fdr 1e-05), [[PIR]] (+0.51, fdr 4e-05), [[SPIN2B]] (+0.50, fdr 3e-05); moves opposite to [[TADA3]] (-0.53, fdr 5e-05), [[SYAP1]] (-0.51, fdr 4e-05), [[BLZF1]] (-0.49, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +6.8 | 5e-09 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.3 | 4e-05 | 1/9 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +4.9 | 2e-04 | 8/33 (AsPC-1, SW1417, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +4.9 | 2e-04 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.002 | 8/41 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +4.1 | 0.005 | 3/9 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.060 | 4/34 (RPMI-7951, A498, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.069 | 4/39 (NCI-H1573, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.2 | 0.069 | 3/25 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.31×** | +3.2 | 0.069 | 0/42 | top dose only | low cells (technical?) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.44×** | +3.1 | 0.096 | 3/25 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.43× | +3.1 | 0.10 | 4/9 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.97× | +3.0 | 0.10 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.493×** | -6.2 | 4e-07 | 20/44 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -5.8 | 2e-06 | 14/37 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.652×** | -5.3 | 2e-05 | 17/29 (LS 180, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -4.8 | 2e-04 | 15/30 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.646×** | -3.7 | 0.024 | 12/36 (A498, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.688×** | -3.3 | 0.093 | 8/18 (LoVo, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.13 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -11.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0764× (z -9.2) |
| [[LS 180 (line)]] | wt | 5.14 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -14.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 2.27 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0567× (z -8.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 2.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.758 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A5]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PIR]] | +0.51 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SPIN2B]] | +0.50 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[GSTA4]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[P3H2-AS1]] | +0.49 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[CYP4F11]] | +0.49 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PIK3C2B]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NMRAL2P-1]] | +0.48 | +0.39 / +0.39 | both halves | 5e-05 |  |
| [[MGST1]] | +0.47 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[HTR1D]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[CYP4F3]] | +0.46 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[MCM3AP-AS1]] | +0.46 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA3]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[SYAP1]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[BLZF1]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[AKAP12]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TLN1]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[USE1]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ODF2]] | -0.46 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[PITPNC1]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ARPC2]] | -0.46 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[RECQL]] | -0.44 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[RB1]] | -0.44 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[HMGA2]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIR]] | B | PIR activity raises GSEC's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without PIR | 0.026 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TRIM16L]] | B | TRIM16L activity raises GSEC's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without TRIM16L | 0.064 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[VEGFD]] | B | VEGFD activity raises GSEC's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.15× lower at baseline in the lines without VEGFD | 0.079 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[MYADM]] | C | MYADM activity strengthens GSEC's drug response | lines that do not express MYADM (3) vs lines expressing it (41) | the lines without MYADM respond 1.19× as strongly (z diff -0.33); strongest at Dinaciclib 0.5 µM: 0.24x vs 1.38x (z diff +5.8) | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction -0.346). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, 44.5); signed map (53.0, -9.0). **Vector** length 40.9, 4.64% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.2 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | G-quadruplex forming sequence containing lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q24.2 — chr11:126,340,882-126,355,587 (-) |
| Ensembl biotype | lncRNA |
| Also known as | GESP, DCPS-AS1, FLJ39051; previously ST3GAL4-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48645) · Entrez [399972](https://www.ncbi.nlm.nih.gov/gene/399972) · Ensembl [ENSG00000280832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280832)

## Data

Gene col 15969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15969); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15969]; `tensor/DDL_lfc|DDL_z.npy` [15969]; `embed/gene_vectors.npy` [15969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15969 or target_col == 15969). Every well: [[GSEC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSEC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
