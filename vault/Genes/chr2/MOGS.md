---
symbol: "MOGS"
type: "gene"
col: 3649
ensembl_id: "ENSG00000115275"
name: "mannosyl-oligosaccharide glucosidase"
location: "2p13.1"
module: 40
arm: "+"
pooled_cpm: 14.38
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# MOGS

*mannosyl-oligosaccharide glucosidase* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.33× (z +4.7, q 0.002, up in 16 of 42 measured lines) ⚠ toxic.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -20.8, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYVN1]] (+0.71, fdr 7e-06), [[IER3IP1]] (+0.69, fdr 7e-06), [[P3H1]] (+0.69, fdr 7e-06); moves opposite to [[DARS1]] (-0.61, fdr 1e-05), [[LZIC]] (-0.57, fdr 1e-05), [[ATRX]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.7 | 0.002 | 16/42 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.0 | 0.66 | 5/48 (SNU-423, LOX-IMVI, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.417×** | -20.8 | 0e+00 | 40/47 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -16.0 | 0e+00 | 41/47 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -10.2 | 3e-22 | 39/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.518×** | -9.3 | 2e-18 | 32/47 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.631×** | -7.7 | 1e-12 | 33/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -7.5 | 5e-12 | 30/47 (HS-578T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.682×** | -6.4 | 1e-08 | 24/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.705×** | -5.9 | 3e-07 | 23/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -5.8 | 3e-07 | 24/46 (SW 900, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -5.7 | 7e-07 | 26/46 (HOP62, SHP-77, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.001 | 16/46 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.766×** | -4.1 | 0.002 | 15/44 (H4, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.800×** | -3.7 | 0.008 | 15/47 (SW 900, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.822×** | -3.3 | 0.043 | 9/48 (SW 900, SW 1088, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 15.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -9.9) |
| [[A498 (line)]] | wt | 20.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.5) |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -17.6) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.9) |
| [[C32 (line)]] | wt | 7.95 | 0 | 2 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0852× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0696× (z -9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.1) |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0351× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.107× (z -9.6) |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.1) |
| [[J82 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.9) |
| [[KATO III (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.1) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.6) |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0779× (z -11.6) |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0994× (z -9.6) |
| [[SNU-423 (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0733× (z -13.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.6) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYVN1]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[IER3IP1]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[P3H1]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.69 | +0.75 / +0.65 | both halves | 7e-06 | STRING 634 |
| [[MGAT1]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 452 |
| [[ARFGAP1]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 960 |
| [[YIPF2]] | +0.66 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[DDB1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.65 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[GPR107]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GGCX]] | +0.65 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[SURF4]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[LZIC]] | -0.57 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ATRX]] | -0.55 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.55 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[METTL18]] | -0.53 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[DNAJC8]] | -0.53 | -0.61 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MOGS's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises MOGS's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.8, -30.6); signed map (-52.3, 5.5). **Vector** length 78.6, 14.4% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -16.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -20.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mannosyl-oligosaccharide glucosidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,461,057-74,465,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCS1, CWH41, DER7 |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Reactome | 22 pathways, smallest: Maturation of spike protein_9683686; Diseases associated with N-glycosylation of proteins; Translation of Structural Proteins_9683701 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13724](https://www.uniprot.org/uniprotkb/Q13724) (Mannosyl-oligosaccharide glucosidase):

> In the context of N-glycan degradation, cleaves the distal alpha 1,2-linked glucose residue from the Glc(3)Man(9)GlcNAc(2) oligosaccharide precursor in a highly specific manner.

**Summary**, from NCBI Gene [7841](https://www.ncbi.nlm.nih.gov/gene/7841):

> This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:24862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24862) · Entrez [7841](https://www.ncbi.nlm.nih.gov/gene/7841) · UniProt [Q13724](https://www.uniprot.org/uniprotkb/Q13724) · Ensembl [ENSG00000115275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115275)

## Data

Gene col 3649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3649); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3649]; `tensor/DDL_lfc|DDL_z.npy` [3649]; `embed/gene_vectors.npy` [3649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3649 or target_col == 3649). Every well: [[MOGS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOGS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
