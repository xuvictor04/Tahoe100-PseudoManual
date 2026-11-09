---
symbol: "ATP2A1"
type: "gene"
col: 12174
ensembl_id: "ENSG00000196296"
name: "ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 1"
location: "16p11.2"
module: 38
arm: "+"
pooled_cpm: 7.38
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ATP2A1

*ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +8.5, q 1e-14, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.326× (z -13.7, q 4e-40, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCE1L]] (+0.81, fdr 7e-06), [[ISY1-RAB43]] (+0.81, fdr 7e-06), [[SRRM5]] (+0.79, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.5 | 1e-14 | 28/45 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.2 | 2e-07 | 17/37 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[EX229 (drug)]] 5 µM |  | **1.96×** | +4.5 | 0.002 | 4/42 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | 1.30× | +3.3 | 0.12 | 9/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.44× | +3.3 | 0.12 | 3/39 (HT-29, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.28× | +3.1 | 0.17 | 10/43 (LS 180, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.326×** | -13.7 | 4e-40 | 38/45 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.455×** | -10.0 | 3e-21 | 35/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.8 | 1e-06 | 20/47 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -5.7 | 1e-06 | 23/44 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.627×** | -5.7 | 1e-06 | 24/45 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.642×** | -5.4 | 5e-06 | 21/44 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -4.6 | 3e-04 | 18/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -4.5 | 5e-04 | 18/45 (HS-578T, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.782×** | -4.4 | 5e-04 | 16/43 (KATO III, HEC-1-A, …) | all doses, flat | composition shift |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.717×** | -4.1 | 0.003 | 11/45 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -3.9 | 0.005 | 18/45 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.600×** | -3.4 | 0.031 | 12/39 (C-33 A, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.032 | 8/46 (RPMI-7951, NCI-H661, …) | top dose only | plate-row cell shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.772×** | -3.2 | 0.058 | 16/39 (HepG2/C3A, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.790×** | -3.0 | 0.096 | 15/43 (SW480, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 10.4 | 0 | 2 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0751× (z -9.8) |
| [[A-172 (line)]] | wt | 7.66 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.103× (z -9.6) |
| [[A498 (line)]] | wt | 6.81 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -9.8) |
| [[C32 (line)]] | wt | 6.82 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0645× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0762× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0852× (z -9.5) |
| [[KATO III (line)]] | alt | 15.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -11.8) |
| [[LoVo (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 7.76 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0826× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 4.86 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0759× (z -9.1) |
| [[RKO (line)]] | wt | 10.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0968× (z -10.8) |
| [[SW480 (line)]] | alt | 6.49 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.184× (z -10.3) |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCE1L]] | +0.81 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ISY1-RAB43]] | +0.81 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SRRM5]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[VWCE]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[PYGM]] | +0.73 | +0.71 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 581 |
| [[HYAL1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.71 | +0.65 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises ATP2A1's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without ASGR1 | 0.044 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[METTL21EP-1]] | C | METTL21EP-1 activity lowers ATP2A1's level | lines that do not express METTL21EP-1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without METTL21EP-1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEMIP2, SMAD7, CASP4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -19.5); signed map (12.9, 11.7). **Vector** length 81.5, 14.6% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -13.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,878,405-28,904,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SERCA1; previously ATP2A |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Hallmark sets | MYOGENESIS |
| Reactome | 13 pathways, smallest: Reduction of cytosolic Ca++ levels; Pre-NOTCH Processing in Golgi; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O14983](https://www.uniprot.org/uniprotkb/O14983) (Sarcoplasmic/endoplasmic reticulum calcium ATPase 1):

> Key regulator of striated muscle performance by acting as the major Ca(2+) ATPase responsible for the reuptake of cytosolic Ca(2+) into the sarcoplasmic reticulum. Catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen (By similarity). Contributes to calcium sequestration involved in muscular excitation/contraction.

**Summary**, from NCBI Gene [487](https://www.ncbi.nlm.nih.gov/gene/487):

> This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of muscle cells. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen, and is involved in muscular excitation and contraction. Mutations in this gene cause some autosomal recessive forms of Brody disease, characterized by increasing impairment of muscular relaxation during …

**Accessions** — [HGNC:811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:811) · Entrez [487](https://www.ncbi.nlm.nih.gov/gene/487) · UniProt [O14983](https://www.uniprot.org/uniprotkb/O14983) · Ensembl [ENSG00000196296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196296)

## Data

Gene col 12174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12174); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12174]; `tensor/DDL_lfc|DDL_z.npy` [12174]; `embed/gene_vectors.npy` [12174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12174 or target_col == 12174). Every well: [[ATP2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
