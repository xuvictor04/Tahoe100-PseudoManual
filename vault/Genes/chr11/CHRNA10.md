---
symbol: "CHRNA10"
type: "gene"
col: 5001
ensembl_id: "ENSG00000129749"
name: "cholinergic receptor nicotinic alpha 10 subunit"
location: "11p15.4"
module: 47
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CHRNA10

*cholinergic receptor nicotinic alpha 10 subunit* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.96× (z +15.6, q 0e+00, up in 25 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.533× (z -5.1, q 2e-04, down in 12 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0505×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.102×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHX3]] (+0.78, fdr 7e-06), [[TTC36]] (+0.76, fdr 7e-06), [[MSANTD1]] (+0.75, fdr 7e-06); moves opposite to [[RCOR3]] (-0.61, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00334]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.96×** | +15.6 | 0e+00 | 25/29 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +8.8 | 4e-16 | 37/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +6.8 | 1e-09 | 17/24 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +6.8 | 1e-09 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +6.4 | 2e-08 | 22/42 (COLO 205, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.2 | 7e-08 | 9/25 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +5.4 | 6e-06 | 15/40 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +5.0 | 5e-05 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.73×** | +4.4 | 8e-04 | 4/45 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.020 | 2/38 (HEC-1-A, A498) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.59×** | +3.5 | 0.024 | 5/38 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +3.2 | 0.057 | 3/44 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.057 | 2/17 (PANC-1, AsPC-1) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.080 | 2/42 (HT-29, hTERT-HPNE) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0505×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.102×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.533×** | -5.1 | 2e-04 | 12/44 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -3.7 | 0.060 | 9/15 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.642× | -3.2 | 0.28 | 12/18 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.40 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0505× (z -12.8) |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.547 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.791 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHX3]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TTC36]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CHADL]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PILRA]] | +0.75 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[MPP4]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[OIT3]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00334]] | B | LINC00334 activity raises CHRNA10's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without LINC00334 | 0.058 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CHRNA10's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CHRNA10's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.261 over the table, 0.017 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | CHRNA10's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | CHRNA10's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.421 over the table, 0.058 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Menadione (drug)]] 0.5 µM | C | CHRNA10's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | CHRNA10's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.426 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.1, -14.5); signed map (17.7, 11.3). **Vector** length 47.3, 5.65% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +6.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor nicotinic alpha 10 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,665,587-3,671,384 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cholinergic receptors nicotinic subunits |
| Reactome | 4 pathways, smallest: Acetylcholine inhibits contraction of outer hair cells; Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZZ6](https://www.uniprot.org/uniprotkb/Q9GZZ6) (Neuronal acetylcholine receptor subunit alpha-10):

> Component of neuronal acetylcholine receptors (nAChRs) that function as pentameric, ligand-gated cation channels with high calcium permeability. nAChRs are excitatory neurotrasnmitter receptors formed by a collection of nAChR subunits. Each nAchR subunit confers differential attributes to channel properties, including activation, deactivation and desensitization kinetics, pH sensitivity, cation permeability, and binding to allosteric modulators (Probable). Forms heteropentamers with CHRNA9. …

**Summary**, from NCBI Gene [57053](https://www.ncbi.nlm.nih.gov/gene/57053):

> Contributes to acetylcholine-gated monoatomic cation-selective channel activity. Involved in acetylcholine receptor signaling pathway and membrane depolarization. Acts upstream of or within positive regulation of cytosolic calcium ion concentration. Part of acetylcholine-gated channel complex. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13800) · Entrez [57053](https://www.ncbi.nlm.nih.gov/gene/57053) · UniProt [Q9GZZ6](https://www.uniprot.org/uniprotkb/Q9GZZ6) · Ensembl [ENSG00000129749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129749)

## Data

Gene col 5001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5001); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5001]; `tensor/DDL_lfc|DDL_z.npy` [5001]; `embed/gene_vectors.npy` [5001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5001 or target_col == 5001). Every well: [[CHRNA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRNA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
