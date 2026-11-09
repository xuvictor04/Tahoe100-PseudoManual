---
symbol: "IDH3G"
type: "gene"
col: 870
ensembl_id: "ENSG00000067829"
name: "isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit gamma"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 15.59
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# IDH3G

*isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit gamma* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +11.3, q 6e-27, up in 35 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.55× (z +3.4, q 0.064, up in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.69×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.730× (z -5.4, q 5e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFKL]] (+0.65, fdr 7e-06), [[MAN1B1]] (+0.62, fdr 1e-05), [[GPS1]] (+0.57, fdr 1e-05); moves opposite to [[PABPN1]] (-0.46, fdr 9e-05), [[LINC00106]] (-0.46, fdr 1e-04), [[EIF5B]] (-0.45, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.69×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.3 | 6e-27 | 35/35 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.6 | 2e-15 | 24/28 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.9 | 1e-09 | 25/32 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.0 | 6e-05 | 3/48 (KATO III, SW 900, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.064 | 16/43 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.17 | 11/44 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -5.4 | 5e-05 | 25/47 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.739×** | -5.1 | 8e-05 | 25/48 (Panc 03.27, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.680×** | -4.6 | 7e-04 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -4.0 | 0.010 | 20/45 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.017 | 19/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.755× | -3.3 | 0.11 | 17/46 (PANC-1, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.758× | -3.1 | 0.16 | 14/47 (H4, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.776× | -3.0 | 0.16 | 12/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.3) |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 9.69 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0815× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.168× (z -10.9) |
| [[A-172 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFKL]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 517 |
| [[MAN1B1]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[GPS1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FASTK]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PLOD1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TMEM214]] | +0.56 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[NOC4L]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PCIF1]] | +0.55 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TRAF7]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[MTFR1L]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SNX17]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CORO1B]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABPN1]] | -0.46 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[LINC00106]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[EIF5B]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SSB]] | -0.44 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ZBTB7A]] | -0.44 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[SMIM30]] | -0.43 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises IDH3G's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.357). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-18.4, -22.1); signed map (-50.7, -12.4). **Vector** length 62.0, 10.9% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.4 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.1 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.0 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -4.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,785,766-153,794,512 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Isocitrate dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Citric acid cycle (TCA cycle); Mitochondrial protein import; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P51553](https://www.uniprot.org/uniprotkb/P51553) (Isocitrate dehydrogenase):

> Regulatory subunit which plays a role in the allosteric regulation of the enzyme catalyzing the decarboxylation of isocitrate (ICT) into alpha-ketoglutarate. The heterodimer composed of the alpha (IDH3A) and beta (IDH3B) subunits and the heterodimer composed of the alpha (IDH3A) and gamma (IDH3G) subunits, have considerable basal activity but the full activity of the heterotetramer (containing two subunits of IDH3A, one of IDH3B and one of IDH3G) requires the assembly and cooperative function …

**Summary**, from NCBI Gene [3421](https://www.ncbi.nlm.nih.gov/gene/3421):

> Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isocitrate dehydrogenases, one of which is mitochondrial and the other predominantly cytosolic. …

**Accessions** — [HGNC:5386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5386) · Entrez [3421](https://www.ncbi.nlm.nih.gov/gene/3421) · UniProt [P51553](https://www.uniprot.org/uniprotkb/P51553) · Ensembl [ENSG00000067829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067829)

## Data

Gene col 870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 870); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 870]; `tensor/DDL_lfc|DDL_z.npy` [870]; `embed/gene_vectors.npy` [870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 870 or target_col == 870). Every well: [[IDH3G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDH3G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
