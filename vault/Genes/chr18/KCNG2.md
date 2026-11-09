---
symbol: "KCNG2"
type: "gene"
col: 10919
ensembl_id: "ENSG00000178342"
name: "potassium voltage-gated channel modifier subfamily G member 2"
location: "18q23"
module: 98
arm: "+"
pooled_cpm: 2.26
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# KCNG2

*potassium voltage-gated channel modifier subfamily G member 2* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.43× (z +16.3, q 0e+00, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.519× (z -4.7, q 0.001, down in 14 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0336×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.200×); [[Tofacitinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.114×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JPH2]] (+0.61, fdr 7e-06), [[ADGRG2]] (+0.60, fdr 1e-05), [[RIPOR2]] (+0.60, fdr 4e-05); moves opposite to [[TTC8]] (-0.42, fdr 5e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PRSS23-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.43×** | +16.3 | 0e+00 | 20/24 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +11.1 | 5e-26 | 2/5 (A498, PANC-1) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.99×** | +10.4 | 3e-23 | 0/2 | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.07×** | +10.1 | 1e-21 | 0/2 | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +9.1 | 1e-17 | 11/24 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +6.2 | 5e-08 | 11/24 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.69×** | +5.3 | 1e-05 | 6/24 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.98×** | +5.3 | 1e-05 | 18/41 (PANC-1, CHP-212, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +5.2 | 1e-05 | 12/36 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +4.5 | 3e-04 | 5/39 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.79×** | +4.5 | 3e-04 | 9/31 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 6e-04 | 6/20 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.73×** | +4.2 | 0.001 | 8/29 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +4.0 | 0.002 | 7/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.68×** | +4.0 | 0.002 | 7/20 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.007 | 4/20 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.009 | 0/12 | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.53×** | +3.0 | 0.067 | 0/6 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +2.9 | 0.091 | 8/22 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +2.8 | 0.097 | 4/38 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0336×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.200×); [[Tofacitinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.519×** | -4.7 | 0.001 | 14/42 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.674× | -3.1 | 0.31 | 7/20 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.670× | -3.1 | 0.31 | 8/36 (LS 180, A549, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.632× | -3.0 | 0.31 | 8/22 (MIA PaCa-2, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0336× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.9) |
| [[A-172 (line)]] | wt | 0.810 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.890 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.893 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.641 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.738 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.905 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.899 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.720 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.577 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.845 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.575 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPH2]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG2]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.60 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[MTMR7]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ITGA10]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PID1]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RTN1]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SLC2A14]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CAVIN2]] | +0.56 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SAA1]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.55 | +0.46 / +0.66 | both halves | 2e-05 | same gene group; pathway: Glucagon-like Peptide-1 (GLP1) regulates insulin secretion |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC8]] | -0.42 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23-AS1]] | C | KCNG2's natural level weakens PRSS23-AS1's drug response | KCNG2's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.27; direction clear | 0.081 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, 17.2); signed map (18.6, 31.4). **Vector** length 43.3, 5.80% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.7 | +4.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +4.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel modifier subfamily G member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,797,938-79,900,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv6.2, KCNF2 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 6 pathways, smallest: Voltage gated Potassium channels; Glucagon-like Peptide-1 (GLP1) regulates insulin secretion; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ96](https://www.uniprot.org/uniprotkb/Q9UJ96) (Voltage-gated potassium channel regulatory subunit KCNG2):

> Regulatory alpha-subunit of the voltage-gated potassium (Kv) channel which, when coassembled with KCNB1, can modulate the kinetics and conductance-voltage relationship. Modulates channel activity by shifting the threshold and the half-maximal activation to more negative values (Probable). Potassium channel subunit that does not form functional channels by itself (Probable).

**Summary**, from NCBI Gene [26251](https://www.ncbi.nlm.nih.gov/gene/26251):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily G. This member is a gamma subunit of the voltage-gated potassium …

**Accessions** — [HGNC:6249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6249) · Entrez [26251](https://www.ncbi.nlm.nih.gov/gene/26251) · UniProt [Q9UJ96](https://www.uniprot.org/uniprotkb/Q9UJ96) · Ensembl [ENSG00000178342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178342)

## Data

Gene col 10919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10919); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10919]; `tensor/DDL_lfc|DDL_z.npy` [10919]; `embed/gene_vectors.npy` [10919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10919 or target_col == 10919). Every well: [[KCNG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
