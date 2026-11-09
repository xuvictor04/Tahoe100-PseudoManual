---
symbol: "ANKRD37"
type: "gene"
col: 11808
ensembl_id: "ENSG00000186352"
name: "ankyrin repeat domain 37"
location: "4q35.1"
module: 79
arm: "+"
pooled_cpm: 59.95
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ANKRD37

*ankyrin repeat domain 37* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Dimethyl fumarate (drug)]] 5 µM: 2.36× (z +4.3, q 0.009, up in 42 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 8.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.292× (z -9.1, q 8e-17, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HILPDA]] (+0.81, fdr 7e-06), [[NDRG1]] (+0.80, fdr 7e-06), [[INSIG2]] (+0.79, fdr 7e-06); moves opposite to [[UTP20]] (-0.74, fdr 7e-06), [[ZMYND11]] (-0.72, fdr 7e-06), [[DNAJC11]] (-0.68, fdr 7e-06).
> It is in [[Module 079]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 8.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | **2.36×** | +4.3 | 0.009 | 42/47 (SW48, HOP62, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.047 | 30/46 (SK-MEL-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.292×** | -9.1 | 8e-17 | 41/45 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.233×** | -7.6 | 1e-11 | 38/45 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.269×** | -6.6 | 1e-08 | 42/45 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.339×** | -5.4 | 9e-06 | 34/45 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.370×** | -5.2 | 3e-05 | 42/46 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -4.3 | 0.002 | 26/38 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.091 | 30/46 (A-172, SW 1271, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.538×** | -3.2 | 0.091 | 27/46 (NCI-H2347, HepG2/C3A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 0.658× | -3.1 | 0.12 | 29/46 (SW 1271, SW48, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.528× | -3.1 | 0.12 | 22/39 (BT-474, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.555× | -3.1 | 0.12 | 23/46 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.301× | -3.0 | 0.12 | 30/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.93 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 227 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -19.8) |
| [[A-172 (line)]] | wt | 61.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 234 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 8.94× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 33.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.7) |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0362× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.8) |
| [[C32 (line)]] | wt | 76.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.3) |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0688× (z -9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.5) |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.6) |
| [[C-33 A (line)]] | alt | 69.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0969× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.0) |
| [[H4 (line)]] | wt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0835× (z -8.9) |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.1) |
| [[KATO III (line)]] | alt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 68.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.5) |
| [[LS 180 (line)]] | wt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 66.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0860× (z -11.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 41.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -9.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 77.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0809× (z -9.7) |
| [[SW 1271 (line)]] | alt | 174 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -12.9) |
| [[SW1417 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 66.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.8) |
| [[A-427 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HILPDA]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[NDRG1]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 | STRING 425 |
| [[INSIG2]] | +0.79 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.79 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[AFMID]] | +0.77 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.77 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[MXI1]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 | STRING 443 |
| [[PDK3]] | +0.74 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.74 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[ZMYND11]] | -0.72 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.68 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[COA7]] | -0.67 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[AVEN]] | -0.66 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD40]] | -0.66 | -0.64 / -0.54 | both halves | 1e-05 | same gene group |
| [[DLG5]] | -0.66 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.65 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[EXOSC10]] | -0.65 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MAPKAPK5]] | -0.65 | -0.50 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -15.6); signed map (-34.8, 23.5). **Vector** length 146, 53.0% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.60 to 16); *glycolysis* (hallmark, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +0.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.4 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,396,021-185,400,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Lrp2bp |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q7Z713](https://www.uniprot.org/uniprotkb/Q7Z713) carries no function annotation.

**Summary**, from NCBI Gene [353322](https://www.ncbi.nlm.nih.gov/gene/353322):

> Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29593) · Entrez [353322](https://www.ncbi.nlm.nih.gov/gene/353322) · UniProt [Q7Z713](https://www.uniprot.org/uniprotkb/Q7Z713) · Ensembl [ENSG00000186352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186352)

## Data

Gene col 11808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11808); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11808]; `tensor/DDL_lfc|DDL_z.npy` [11808]; `embed/gene_vectors.npy` [11808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11808 or target_col == 11808). Every well: [[ANKRD37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
