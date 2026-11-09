---
symbol: "ZNG1F"
type: "gene"
col: 13247
ensembl_id: "ENSG00000215126"
name: "Zn regulated GTPase metalloprotein activator 1F"
location: "9p11.2"
module: 5
arm: "+"
pooled_cpm: 7.13
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ZNG1F

*Zn regulated GTPase metalloprotein activator 1F* — 9p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.15× (z +7.3, q 1e-10, up in 15 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.36× (z +6.3, q 5e-08, up in 16 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.583× (z -4.2, q 0.016, down in 10 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HOP62 0.133×, MIA PaCa-2 0.128×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Apalutamide (drug)]] 0.05 µM in 1 line (HS-578T 0.0536×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW48 0.0782×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1E]] (+0.82, fdr 7e-06), [[ZNG1C]] (+0.76, fdr 7e-06), [[METTL2B]] (+0.62, fdr 1e-05); moves opposite to [[SERINC1]] (-0.55, fdr 1e-05), [[LMBRD1]] (-0.54, fdr 1e-05), [[MKRN1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARVB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.3 | 1e-10 | 15/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +6.9 | 1e-09 | 17/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +6.3 | 5e-08 | 16/42 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.1 | 1e-07 | 15/41 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.4 | 9e-06 | 16/46 (SHP-77, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +4.5 | 6e-04 | 9/46 (SHP-77, Hs 766T, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HOP62 0.133×, MIA PaCa-2 0.128×; ⚠ transcription drop; cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Apalutamide (drug)]] 0.05 µM in 1 line (HS-578T 0.0536×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW48 0.0782×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -4.2 | 0.016 | 10/44 (SHP-77, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.763× | -3.3 | 0.19 | 10/45 (KATO III, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Talc (drug)]] 0.5 µM |  | 0.802× | -3.3 | 0.19 | 7/44 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.864× | -3.1 | 0.24 | 11/45 (KATO III, Hs 766T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | 0.814× | -3.1 | 0.24 | 13/33 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.26 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.133× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 4.86 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0536× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SW48 (line)]] | wt | 9.50 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0782× (z -8.8) |
| [[SW480 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1E]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ZNG1C]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[METTL2B]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[MECR]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNG1B]] | +0.59 | +0.68 / +0.51 | both halves | 1e-05 | STRING 828 |
| [[PUS1]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EXOSC7]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DDX19A]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[NSUN4]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PIGL]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.56 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[FBXW8]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC1]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[LMBRD1]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MKRN1]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[USP33]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NEK7]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PDE5A]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[FXR1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CAPZA2]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PPM1A]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SVBP]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GM2A]] | -0.48 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[H3-3A]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVB]] | B | PARVB activity raises ZNG1F's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.13× lower at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[HDAC6]] | B | HDAC6 activity lowers ZNG1F's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -41.5); signed map (1.8, -53.9). **Vector** length 50.1, 6.22% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.1 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | Zn regulated GTPase metalloprotein activator 1F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p11.2 — chr9:41,131,306-41,199,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OTTHUMG00000066820, OTTHUMG00000067194; previously CBWD7, CBWD6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4V339](https://www.uniprot.org/uniprotkb/Q4V339) (Zinc-regulated GTPase metalloprotein activator 1F):

> Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them (By similarity). Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1 (By similarity). After formation of the docked complex, zinc is transferred from …

**Summary**, from NCBI Gene [644019](https://www.ncbi.nlm.nih.gov/gene/644019):

> Predicted to enable zinc chaperone activity and zinc ion binding activity. Predicted to be involved in protein maturation. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31978) · Entrez [644019](https://www.ncbi.nlm.nih.gov/gene/644019) · UniProt [Q4V339](https://www.uniprot.org/uniprotkb/Q4V339) · Ensembl [ENSG00000215126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215126)

## Data

Gene col 13247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13247); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13247]; `tensor/DDL_lfc|DDL_z.npy` [13247]; `embed/gene_vectors.npy` [13247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13247 or target_col == 13247). Every well: [[ZNG1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNG1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
