---
symbol: "VPS11"
type: "gene"
col: 8369
ensembl_id: "ENSG00000160695"
name: "VPS11 core subunit of CORVET and HOPS complexes"
location: "11q23.3"
module: 122
arm: "+"
pooled_cpm: 15.03
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# VPS11

*VPS11 core subunit of CORVET and HOPS complexes* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +17.1, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.748× (z -7.6, q 1e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMCR8]] (+0.69, fdr 7e-06), [[ALG1]] (+0.68, fdr 1e-05), [[GPATCH3]] (+0.68, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +17.1 | 0e+00 | 39/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.07×** | +13.5 | 8e-39 | 43/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +11.3 | 2e-27 | 34/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +9.1 | 2e-17 | 33/48 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.8 | 2e-16 | 24/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +8.0 | 1e-13 | 34/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +7.9 | 2e-13 | 31/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.8 | 3e-13 | 31/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.8 | 5e-13 | 28/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 6e-11 | 27/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 2e-09 | 23/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 2e-09 | 20/47 (PANC-1, A-427, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.4 | 9e-09 | 17/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.0 | 6e-08 | 19/47 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.0 | 1e-07 | 21/46 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.7 | 4e-07 | 21/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -7.6 | 1e-11 | 30/48 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.690×** | -6.9 | 2e-09 | 26/47 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.648×** | -4.2 | 0.005 | 13/45 (H4, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.812×** | -3.7 | 0.028 | 16/43 (SNU-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.889× | -3.1 | 0.19 | 8/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 16.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +16.9) | — |
| [[Hs 766T (line)]] | wt | 17.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[KATO III (line)]] | alt | 28.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.8) | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.146× (z -9.0) ⚠ toxic |
| [[A498 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[BT-474 (line)]] | alt | 8.89 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0823× (z -10.5) |
| [[COLO 205 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.182× (z -8.8) |
| [[HS-578T (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.7) | — |
| [[J82 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 8.12 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0774× (z -11.0) |
| [[SNU-423 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.5) | — |
| [[SW480 (line)]] | alt | 20.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +9.0) | — |
| [[A-172 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMCR8]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ALG1]] | +0.68 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.68 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[HEXA]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[GET3]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TPP1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[ATP6V1C1]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TSC1]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MED12]] | +0.63 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.5, 13.5); signed map (-9.5, -20.1). **Vector** length 75.3, 13.1% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +11.3 |
|  | [[NG25 (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +17.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +6.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.9 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | VPS11 core subunit of CORVET and HOPS complexes |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,067,818-119,081,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF108, PEP5 |
| Gene groups (HGNC) | Ring finger proteins; HOPS complex; CORVET complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H270](https://www.uniprot.org/uniprotkb/Q9H270) (Vacuolar protein sorting-associated protein 11 homolog):

> Plays a role in vesicle-mediated protein trafficking to lysosomal compartments including the endocytic membrane transport and autophagic pathways. Believed to act as a core component of the putative HOPS and CORVET endosomal tethering complexes which are proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The HOPS complex is proposed …

**Summary**, from NCBI Gene [55823](https://www.ncbi.nlm.nih.gov/gene/55823):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late endosomes/lysosomes, and like their yeast counterparts, may mediate vesicle trafficking steps in …

**Accessions** — [HGNC:14583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14583) · Entrez [55823](https://www.ncbi.nlm.nih.gov/gene/55823) · UniProt [Q9H270](https://www.uniprot.org/uniprotkb/Q9H270) · Ensembl [ENSG00000160695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160695)

## Data

Gene col 8369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8369); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8369]; `tensor/DDL_lfc|DDL_z.npy` [8369]; `embed/gene_vectors.npy` [8369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8369 or target_col == 8369). Every well: [[VPS11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
