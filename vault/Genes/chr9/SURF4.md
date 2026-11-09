---
symbol: "SURF4"
type: "gene"
col: 7256
ensembl_id: "ENSG00000148248"
name: "surfeit 4"
location: "9q34.2"
module: 42
arm: "+"
pooled_cpm: 95.34
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SURF4

*surfeit 4* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.78× (z +9.0, q 2e-16, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -12.7, q 4e-34, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A1]] (+0.84, fdr 7e-06), [[SAR1A]] (+0.74, fdr 7e-06), [[GOLT1B]] (+0.73, fdr 7e-06); moves opposite to [[KLF11]] (-0.61, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +9.0 | 2e-16 | 45/48 (HEC-1-A, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +5.6 | 7e-06 | 39/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.9 | 1e-04 | 29/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.008 | 29/48 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.9 | 0.009 | 28/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.021 | 15/49 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.071 | 26/48 (HOP62, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -12.7 | 4e-34 | 42/48 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.507×** | -10.1 | 1e-21 | 47/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -6.5 | 2e-08 | 38/48 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -6.3 | 5e-08 | 35/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.690×** | -5.7 | 1e-06 | 36/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -5.1 | 4e-05 | 33/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -4.5 | 6e-04 | 31/48 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.748×** | -4.5 | 6e-04 | 27/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.2 | 0.001 | 24/48 (SW 900, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -4.1 | 0.002 | 26/48 (A-172, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.837× | -3.7 | 0.010 | 24/48 (HS-578T, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.011 | 24/48 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.014 | 28/48 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.033 | 25/47 (SHP-77, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.041 | 26/48 (CHP-212, SW1417, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.821×** | -3.0 | 0.086 | 21/49 (CFPAC-1, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 107 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -19.2) |
| [[A498 (line)]] | wt | 192 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 82.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.9) |
| [[A-427 (line)]] | wt | 42.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.367× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 78.6 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.70× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.325× (z -10.2) |
| [[A549 (line)]] | wt | 88.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.7) |
| [[J82 (line)]] | alt | 151 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -27.1) |
| [[RKO (line)]] | wt | 194 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -15.0) |
| [[BT-474 (line)]] | alt | 80.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.9) |
| [[C-33 A (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 83.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[H4 (line)]] | wt | 136 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.353× (z -9.1) |
| [[HOP62 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.7) |
| [[HT-29 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 86.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 74.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 69.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.369× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 98.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -9.7) |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0777× (z -10.2) |
| [[SW 900 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.7) |
| [[AN3 CA (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 135 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 107 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A1]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 | STRING 735 |
| [[SAR1A]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | STRING 756 |
| [[GOLT1B]] | +0.73 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SLC39A7]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.73 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[SEC13]] | +0.72 | +0.74 / +0.79 | both halves | 7e-06 | STRING 650 |
| [[ARFGAP1]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 | pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 567 |
| [[SEC24D]] | +0.72 | +0.71 / +0.77 | both halves | 7e-06 | STRING 432 |
| [[KDELR2]] | +0.72 | +0.69 / +0.79 | both halves | 7e-06 | pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 691 |
| [[BET1L]] | +0.72 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[P4HB]] | +0.72 | +0.79 / +0.77 | both halves | 7e-06 | STRING 684 |
| [[MYDGF]] | +0.72 | +0.79 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF11]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -30.5); signed map (-52.6, 7.4). **Vector** length 128, 42.3% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.62 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.56 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.4 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +3.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.5 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -12.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | surfeit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,361,450-133,376,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERV29, FLJ22993, MGC102753 |
| Reactome | 7 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O15260](https://www.uniprot.org/uniprotkb/O15260) (Surfeit locus protein 4):

> Endoplasmic reticulum cargo receptor that mediates the export of lipoproteins by recruiting cargos into COPII vesicles to facilitate their secretion. Acts as a cargo receptor for lipoproteins bearing both APOB and APOA1, thereby regulating lipoprotein delivery and the maintenance of lipid homeostasis. Synergizes with the GTPase SAR1B to mediate transport of circulating lipoproteins. Promotes the secretion of PCSK9. Also mediates the efficient secretion of erythropoietin (EPO). May also play a …

**Summary**, from NCBI Gene [6836](https://www.ncbi.nlm.nih.gov/gene/6836):

> This gene is located in the surfeit gene cluster, which is comprised of very tightly linked housekeeping genes that do not share sequence similarity. The encoded protein is a conserved integral membrane protein that interacts with endoplasmic reticulum-Golgi intermediate compartment proteins. Disruption of this gene results in reduced numbers of endoplasmic reticulum-Golgi intermediate compartment clusters and redistribution of coat protein I to the cytosol. Alternate splicing results in …

**Accessions** — [HGNC:11476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11476) · Entrez [6836](https://www.ncbi.nlm.nih.gov/gene/6836) · UniProt [O15260](https://www.uniprot.org/uniprotkb/O15260) · Ensembl [ENSG00000148248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148248)

## Data

Gene col 7256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7256); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7256]; `tensor/DDL_lfc|DDL_z.npy` [7256]; `embed/gene_vectors.npy` [7256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7256 or target_col == 7256). Every well: [[SURF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SURF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
