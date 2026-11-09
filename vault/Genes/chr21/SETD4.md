---
symbol: "SETD4"
type: "gene"
col: 11752
ensembl_id: "ENSG00000185917"
name: "SET domain containing 4"
location: "21q22.12"
module: 1
arm: "+"
pooled_cpm: 13.86
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SETD4

*SET domain containing 4* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +9.4, q 3e-18, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.716× (z -5.6, q 1e-05, down in 23 of 43 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (A-172 0.137×, LS 180 0.243×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0615×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0866×); [[Delamanid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0710×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.137×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK5]] (+0.69, fdr 1e-05), [[NOL9]] (+0.68, fdr 7e-06), [[WDR73]] (+0.68, fdr 1e-05); moves opposite to [[ARFGAP3]] (-0.56, fdr 3e-05), [[PEAK1]] (-0.55, fdr 2e-05), [[DNAJC1]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +9.4 | 3e-18 | 27/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.9 | 6e-13 | 27/46 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +6.5 | 1e-08 | 21/44 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.2 | 8e-08 | 21/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.27×** | +5.8 | 6e-07 | 18/48 (RKO, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 17/48 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 2e-05 | 20/46 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.35×** | +5.0 | 4e-05 | 15/42 (C32, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.6 | 3e-04 | 9/48 (SW480, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.5 | 4e-04 | 18/47 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.1 | 0.002 | 15/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.24×** | +3.6 | 0.014 | 10/46 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.026 | 10/45 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.085 | 1/47 (LOX-IMVI) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.099 | 9/46 (SW1417, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.099 | 1/45 (A498) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (A-172 0.137×, LS 180 0.243×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (KATO III 0.0615×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.0866×); [[Delamanid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0710×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -5.6 | 1e-05 | 23/43 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.679× | -3.5 | 0.12 | 12/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.2 | 0.27 | 5/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.9) | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0851× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -13.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 9.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +12.7) | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.137× (z -8.6) |
| [[HCT15 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 8.68 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0710× (z -9.3) |
| [[Hs 766T (line)]] | wt | 9.08 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0866× (z -11.0) |
| [[KATO III (line)]] | alt | 8.02 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0615× (z -13.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | +0.69 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NOL9]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[WDR73]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ZBTB45]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SCO1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[DHX30]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GATB]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[VPS52]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.61 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ALKBH3]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP3]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DNAJC1]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-39.9, 12.4); signed map (-9.7, -29.7). **Vector** length 61.0, 8.52% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.1 | -5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:36,034,541-36,079,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C21orf27, C21orf18 |
| Gene groups (HGNC) | SET domain containing; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVD3](https://www.uniprot.org/uniprotkb/Q9NVD3) (SET domain-containing protein 4):

> Protein-lysine N-methyltransferase that methylates both histones and non-histone proteins. Via its catalytic activity, regulates many processes, including cell proliferation, cell differentiation, inflammatory response and apoptosis. Regulates the inflammatory response by mediating mono- and dimethylation of 'Lys-4' of histone H3 (H3K4me1 and H3K4me2, respectively), leading to activate the transcription of pro-inflammatory cytokines IL6 and TNF (By similarity). Through the catalysis of TBK1 …

**Summary**, from NCBI Gene [54093](https://www.ncbi.nlm.nih.gov/gene/54093):

> Enables histone H4K20 methyltransferase activity. Predicted to be involved in several processes, including positive regulation of inflammatory response; regulation of cell proliferation in bone marrow; and regulation of gene expression. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1258) · Entrez [54093](https://www.ncbi.nlm.nih.gov/gene/54093) · UniProt [Q9NVD3](https://www.uniprot.org/uniprotkb/Q9NVD3) · Ensembl [ENSG00000185917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185917)

## Data

Gene col 11752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11752); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11752]; `tensor/DDL_lfc|DDL_z.npy` [11752]; `embed/gene_vectors.npy` [11752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11752 or target_col == 11752). Every well: [[SETD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
