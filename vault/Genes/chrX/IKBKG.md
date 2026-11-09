---
symbol: "IKBKG"
type: "gene"
col: 15620
ensembl_id: "ENSG00000269335"
name: "inhibitor of nuclear factor kappa B kinase regulatory subunit gamma"
location: "Xq28"
module: 127
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# IKBKG

*inhibitor of nuclear factor kappa B kinase regulatory subunit gamma* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.88× (z +6.2, q 2e-07, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.669× (z -4.0, q 0.039, down in 12 of 44 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0671×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (A-427 0.0632×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SNU-423 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF2]] (+0.65, fdr 1e-05), [[CDK9]] (+0.64, fdr 7e-06), [[TOP3B]] (+0.64, fdr 1e-05); moves opposite to [[KBTBD3]] (-0.60, fdr 1e-05), [[ARHGAP12]] (-0.60, fdr 2e-05), [[MAK]] (-0.59, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +6.2 | 2e-07 | 19/44 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +6.2 | 2e-07 | 21/44 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.4 | 1e-05 | 20/40 (HEC-1-A, NCI-H2347, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +5.1 | 5e-05 | 14/40 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +5.0 | 6e-05 | 20/42 (COLO 205, NCI-H1573, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.67×** | +4.8 | 2e-04 | 16/41 (SW480, COLO 205, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +4.2 | 0.002 | 8/33 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.009 | 10/41 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.009 | 2/12 (HOP62, SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.13 | 8/34 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15620.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0671×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (A-427 0.0632×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SNU-423 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.669×** | -4.0 | 0.039 | 12/44 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.705× | -3.5 | 0.13 | 4/45 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.700× | -3.4 | 0.13 | 11/40 (RKO, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.09 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0632× (z -9.0) |
| [[KATO III (line)]] | alt | 5.04 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0671× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.06 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0745× (z -8.8) |
| [[A-172 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CDK9]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TOP3B]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MFN2]] | +0.63 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[NUDC]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZSCAN22]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[HARS1]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 | pathway: Activation of NF-kappaB in B cells |
| [[WASH8P]] ⚠ | +0.60 | +0.55 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NECAB3]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PSMC3]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Activation of NF-kappaB in B cells |
| [[SNX19]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ARHGAP12]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MAK]] | -0.59 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[LCORL]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.56 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[SNX2]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ARID4A]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TBC1D12]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.55 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ORC4]] | -0.55 | -0.36 / -0.62 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers IKBKG's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -27.3); signed map (-14.0, -30.8). **Vector** length 51.6, 6.32% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | +1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of nuclear factor kappa B kinase regulatory subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,541,199-154,565,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKK-gamma, NEMO, Fip3p, FIP-3, FIP3, IKKAP1, IKKG; previously IP2, IP1 |
| Gene groups (HGNC) | IKK complex; Zinc fingers C2HC NEMO-type |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 82 pathways, smallest: IKBKB deficiency causes SCID; IKBKG deficiency causes anhidrotic ectodermal dysplasia with immunodeficiency (EDA-ID) (via TLR); SLC15A4:TASL-dependent IRF5 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6K9](https://www.uniprot.org/uniprotkb/Q9Y6K9) (NF-kappa-B essential modulator):

> Regulatory subunit of the IKK core complex which phosphorylates inhibitors of NF-kappa-B thus leading to the dissociation of the inhibitor/NF-kappa-B complex and ultimately the degradation of the inhibitor. Its binding to scaffolding polyubiquitin plays a key role in IKK activation by multiple signaling receptor pathways. Can recognize and bind both 'Lys-63'-linked and linear polyubiquitin upon cell stimulation, with a much higher affinity for linear polyubiquitin. Could be implicated in …

**Summary**, from NCBI Gene [8517](https://www.ncbi.nlm.nih.gov/gene/8517):

> This gene encodes the regulatory subunit of the inhibitor of kappaB kinase (IKK) complex, which activates NF-kappaB resulting in activation of genes involved in inflammation, immunity, cell survival, and other pathways. Mutations in this gene result in incontinentia pigmenti, hypohidrotic ectodermal dysplasia, and several other types of immunodeficiencies. A pseudogene highly similar to this locus is located in an adjacent region of the X chromosome. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:5961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5961) · Entrez [8517](https://www.ncbi.nlm.nih.gov/gene/8517) · UniProt [Q9Y6K9](https://www.uniprot.org/uniprotkb/Q9Y6K9) · Ensembl [ENSG00000269335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269335)

## Data

Gene col 15620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15620); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15620]; `tensor/DDL_lfc|DDL_z.npy` [15620]; `embed/gene_vectors.npy` [15620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15620 or target_col == 15620). Every well: [[IKBKG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKBKG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
