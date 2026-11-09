---
symbol: "VPS16"
type: "gene"
col: 13259
ensembl_id: "ENSG00000215305"
name: "VPS16 core subunit of CORVET and HOPS complexes"
location: "20p13"
module: 209
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# VPS16

*VPS16 core subunit of CORVET and HOPS complexes* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +10.8, q 1e-24, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.775× (z -4.2, q 0.017, down in 19 of 42 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (LS 180 0.112×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.205×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.149×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM175]] (+0.69, fdr 7e-06), [[ZNF865]] (+0.62, fdr 1e-05), [[C6orf89]] (+0.60, fdr 1e-05); moves opposite to [[IFRD1]] (-0.55, fdr 3e-05), [[LDHC]] (-0.55, fdr 3e-05), [[BZW2]] (-0.51, fdr 3e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +10.8 | 1e-24 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +9.1 | 3e-17 | 32/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +8.8 | 2e-16 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.9 | 6e-10 | 22/34 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.6 | 5e-09 | 14/27 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 6e-05 | 18/46 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.2 | 0.002 | 14/31 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.007 | 13/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.007 | 7/47 (LoVo, J82, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +3.7 | 0.012 | 13/43 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.26×** | +3.7 | 0.012 | 12/40 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.034 | 6/43 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.048 | 5/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.095 | 2/48 (SW480, AsPC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13259.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (LS 180 0.112×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.205×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.149×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -4.2 | 0.017 | 19/42 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.807×** | -3.6 | 0.074 | 5/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.44 | 2/48 (NCI-H23, NCI-H460) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.205× (z -10.5) |
| [[C32 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -9.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 8.23 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.112× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM175]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ZNF865]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[C6orf89]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[C19orf47]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RNF25]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CROCCP2]] | +0.58 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[ASCC2]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[C12orf4]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MRPS14]] | +0.54 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PSMF1]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TBC1D13]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[KCTD2]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD1]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[LDHC]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[BZW2]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[FGF18]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TRIM72]] | -0.50 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[DNAJA1]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[LINC03036]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[FOSB]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CKS2]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[C19orf38]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[IQCN]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[PRKCG]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | VPS16's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | VPS16's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.417 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.8, -4.7); signed map (-13.4, -24.1). **Vector** length 55.1, 7.11% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +2.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.2 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.8 | -4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS16 core subunit of CORVET and HOPS complexes |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,840,703-2,866,732 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HOPS complex; CORVET complex |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H269](https://www.uniprot.org/uniprotkb/Q9H269) (Vacuolar protein sorting-associated protein 16 homolog):

> Plays a role in vesicle-mediated protein trafficking to lysosomal compartments including the endocytic membrane transport and autophagic pathways. Believed to act as a core component of the putative HOPS and CORVET endosomal tethering complexes which are proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The HOPS complex is proposed …

**Summary**, from NCBI Gene [64601](https://www.ncbi.nlm.nih.gov/gene/64601):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps16 protein. The mammalian class C Vps proteins are predominantly associated with late endosomes/lysosomes, and like their yeast counterparts, may mediate vesicle trafficking steps in …

**Accessions** — [HGNC:14584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14584) · Entrez [64601](https://www.ncbi.nlm.nih.gov/gene/64601) · UniProt [Q9H269](https://www.uniprot.org/uniprotkb/Q9H269) · Ensembl [ENSG00000215305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215305)

## Data

Gene col 13259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13259); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13259]; `tensor/DDL_lfc|DDL_z.npy` [13259]; `embed/gene_vectors.npy` [13259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13259 or target_col == 13259). Every well: [[VPS16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
