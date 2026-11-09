---
symbol: "APC2"
type: "gene"
col: 3644
ensembl_id: "ENSG00000115266"
name: "APC regulator of Wnt signaling pathway 2"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# APC2

*APC regulator of Wnt signaling pathway 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.78× (z +16.2, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.668× (z -4.2, q 0.017, down in 16 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0528×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.100×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (LoVo 0.0595×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.72, fdr 7e-06), [[CATSPERD]] (+0.70, fdr 7e-06), [[AZU1]] (+0.70, fdr 7e-06); moves opposite to [[PTAR1]] (-0.51, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.78×** | +16.2 | 0e+00 | 42/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +15.6 | 0e+00 | 25/31 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.73×** | +14.7 | 0e+00 | 29/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.10×** | +14.6 | 0e+00 | 37/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +9.2 | 3e-18 | 21/40 (SW480, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +8.6 | 5e-16 | 23/45 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.25×** | +7.8 | 3e-13 | 19/39 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +7.1 | 8e-11 | 26/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.67×** | +7.0 | 1e-10 | 17/31 (MIA PaCa-2, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.95×** | +6.3 | 2e-08 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.2 | 4e-08 | 16/35 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.6 | 1e-06 | 13/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.66×** | +5.3 | 6e-06 | 3/13 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 7e-06 | 8/45 (Panc 03.27, SW48, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.40×** | +4.8 | 7e-05 | 5/27 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +4.7 | 9e-05 | 11/46 (CHP-212, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 2e-04 | 6/40 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0528×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.100×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (LoVo 0.0595×); [[Pimozide (drug)]] 0.05 µM in 1 line (A498 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 0.017 | 16/42 (C-33 A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | 0.743× | -3.1 | 0.58 | 6/45 (H4, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.87 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +15.0) | [[Pimozide (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[LoVo (line)]] | wt | 2.69 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +9.9) | [[Roxadustat (drug)]] 0.5 µM 0.0595× (z -9.3) |
| [[C32 (line)]] | wt | 3.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.63 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0528× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 7.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 1.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.6) | — |
| [[A-172 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.72 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.70 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[AZU1]] | +0.70 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[KIF17]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[HCN2]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CELF5]] | +0.65 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LHX4]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTAR1]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises APC2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without CHD5 | 0.017 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SSC5D]] | B | SSC5D activity raises APC2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without SSC5D | 0.057 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[KCNQ2]] | B | KCNQ2 activity raises APC2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without KCNQ2 | 0.063 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[CFAP45]] | B | CFAP45 activity lowers APC2's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.78× higher at baseline in the lines without CFAP45 | 0.086 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, -16.0); signed map (17.3, 14.3). **Vector** length 55.9, 7.40% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.5 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | APC regulator of Wnt signaling pathway 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,446,302-1,473,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APCL |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95996](https://www.uniprot.org/uniprotkb/O95996) (Adenomatous polyposis coli protein 2):

> Stabilizes microtubules and may regulate actin fiber dynamics through the activation of Rho family GTPases. May also function in Wnt signaling by promoting the rapid degradation of CTNNB1.

**Summary**, from NCBI Gene [10297](https://www.ncbi.nlm.nih.gov/gene/10297):

> This gene encodes a strongly conserved protein that has an N-terminal coiled-coil domain followed by an armadillo domain, five 20-amino acid repeats, and two SAMP domains. This protein promotes the assembly of a multiprotein complex that recruits and phosphorylates the Wnt effector beta-catenin and targets beta-catenin for ubiquitylation and proteasomal degradation. This protein therefore plays a role in the reduction of cytoplasmic levels of beta-catenin which in turn reduces activation of Wnt …

**Accessions** — [HGNC:24036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24036) · Entrez [10297](https://www.ncbi.nlm.nih.gov/gene/10297) · UniProt [O95996](https://www.uniprot.org/uniprotkb/O95996) · Ensembl [ENSG00000115266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115266)

## Data

Gene col 3644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3644); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3644]; `tensor/DDL_lfc|DDL_z.npy` [3644]; `embed/gene_vectors.npy` [3644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3644 or target_col == 3644). Every well: [[APC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
