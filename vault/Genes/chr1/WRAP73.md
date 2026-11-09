---
symbol: "WRAP73"
type: "gene"
col: 3778
ensembl_id: "ENSG00000116213"
name: "WD repeat containing, antisense to TP73"
location: "1p36.32"
module: 26
arm: "-"
pooled_cpm: 8.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# WRAP73

*WD repeat containing, antisense to TP73* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.82× (z +14.5, q 7e-45, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.569× (z -11.2, q 2e-26, down in 29 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.250×, HOP62 0.276×, HS-578T 0.277×); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STUB1]] (+0.72, fdr 5e-05), [[PUSL1]] (+0.72, fdr 5e-05), [[MRPS34]] (+0.69, fdr 2e-05); moves opposite to [[LRP2BP]] (-0.71, fdr 3e-05), [[HCG17]] (-0.71, fdr 2e-05), [[LHFPL3]] (-0.70, fdr 2e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[XKR8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +14.5 | 7e-45 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +14.4 | 1e-44 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +10.6 | 4e-24 | 40/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.9 | 5e-07 | 19/36 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.001 | 14/43 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +4.3 | 0.002 | 12/47 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.30×** | +3.5 | 0.035 | 10/39 (SHP-77, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.039 | 2/39 (SW480, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.046 | 6/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.27×** | +3.3 | 0.046 | 9/37 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.28×** | +3.3 | 0.049 | 1/16 (HEC-1-A) | top dose only | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.11 | 5/42 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.24× | +3.0 | 0.12 | 9/44 (A-172, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.250×, HOP62 0.276×, HS-578T 0.277×); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -11.2 | 2e-26 | 29/45 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -6.4 | 4e-08 | 22/43 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.790× | -3.2 | 0.26 | 14/44 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.796× | -3.1 | 0.26 | 2/48 (HS-578T, LOX-IMVI) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.07 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.94× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 7.11 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.7) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 6.66 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.2) |
| [[A-172 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | +0.72 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PUSL1]] | +0.72 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[MRPS34]] | +0.69 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SLC39A3]] | +0.69 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[NDUFA12]] | +0.69 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ESS2]] | +0.69 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MAST3]] | +0.68 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[TECPR1]] | +0.68 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PSMD9]] | +0.67 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[RSAD1]] | +0.67 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[POLRMT]] | +0.67 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[RNF41]] | +0.66 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP2BP]] | -0.71 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[HCG17]] | -0.71 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LHFPL3]] | -0.70 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PBLD]] | -0.70 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.69 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[AP4S1]] | -0.69 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CCT6B]] | -0.69 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PCBP1-AS1]] | -0.68 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.68 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | -0.68 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.68 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[UBE2D3-AS1]] | -0.68 | -0.51 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR8]] | B | XKR8 activity lowers WRAP73's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.24× higher at baseline in the lines without XKR8 | 0.087 | ⚠ within organs, on part of the lines; also absent: MORC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.4, 8.7); signed map (-32.4, 2.5). **Vector** length 67.9, 12.1% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +14.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | +1.8 | +4.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat containing, antisense to TP73 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,630,767-3,652,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WDR8 |
| Gene groups (HGNC) | WD repeat domain containing; Centriolar satellite proteins |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2S5](https://www.uniprot.org/uniprotkb/Q9P2S5) (WD repeat-containing protein WRAP73):

> The SSX2IP:WRAP73 complex is proposed to act as regulator of spindle anchoring at the mitotic centrosome. Required for the centrosomal localization of SSX2IP and normal mitotic bipolar spindle morphology. Required for the targeting of centriole satellite proteins to centrosomes such as of PCM1, SSX2IP, CEP290 and PIBF1/CEP90. Required for ciliogenesis and involved in the removal of the CEP97:CCP110 complex from the mother centriole. Involved in ciliary vesicle formation at the mother centriole …

**Summary**, from NCBI Gene [49856](https://www.ncbi.nlm.nih.gov/gene/49856):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Studies of the related mouse protein suggest that the encoded protein may …

**Accessions** — [HGNC:12759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12759) · Entrez [49856](https://www.ncbi.nlm.nih.gov/gene/49856) · UniProt [Q9P2S5](https://www.uniprot.org/uniprotkb/Q9P2S5) · Ensembl [ENSG00000116213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116213)

## Data

Gene col 3778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3778); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3778]; `tensor/DDL_lfc|DDL_z.npy` [3778]; `embed/gene_vectors.npy` [3778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3778 or target_col == 3778). Every well: [[WRAP73 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WRAP73.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
